import json
from pathlib import Path
from flask import Blueprint, current_app, request
from backend.services.database import query, execute
from backend.services.ioc_validator import validate_indicator
from backend.services.enrichment_engine import enrich_indicator
from backend.services.risk_engine import calculate_vulnerability_priority

api=Blueprint("api",__name__)
def db(): return current_app.config["DATABASE_PATH"]

@api.get("/threats")
def threats():
    sql="SELECT t.*, i.indicator_type, i.indicator_value FROM threats t LEFT JOIN indicators i ON t.threat_id=i.threat_id WHERE 1=1"
    args=[]
    for field,col in [("severity","t.severity"),("category","t.category"),("status","t.status"),("indicator_type","i.indicator_type")]:
        if request.args.get(field): sql+=f" AND {col}=?"; args.append(request.args[field])
    if request.args.get("sort")=="risk": sql+=" ORDER BY t.risk_score DESC"
    else: sql+=" ORDER BY t.last_seen DESC"
    return query(db(),sql,args)

@api.get("/threats/<threat_id>")
def threat_detail(threat_id):
    rows=query(db(),"SELECT * FROM threats WHERE threat_id=?",(threat_id,))
    if not rows: return {"error":"Threat not found"},404
    r=rows[0]
    r["indicators"]=query(db(),"SELECT * FROM indicators WHERE threat_id=?",(threat_id,))
    r["attack_mappings"]=query(db(),"SELECT tactic,technique,technique_id_optional FROM attack_mappings WHERE threat_id=?",(threat_id,))
    r["alerts"]=query(db(),"SELECT * FROM alerts WHERE threat_id=?",(threat_id,))
    r["notes"]=query(db(),"SELECT note,created_at FROM analyst_notes WHERE threat_id=? ORDER BY created_at DESC",(threat_id,))
    return r

@api.get("/indicators/search")
def indicator_search():
    value=request.args.get("q","")
    validation=validate_indicator(value)
    if not validation["valid"]: return validation
    rows=query(db(),"SELECT t.*,i.indicator_type,i.indicator_value FROM threats t JOIN indicators i ON t.threat_id=i.threat_id WHERE lower(i.indicator_value)=lower(?)",(validation["normalized_value"],))
    return {"validation":validation, "enrichment":enrich_indicator(validation["normalized_value"],rows, query(db(),"SELECT * FROM alerts"))}

@api.get("/dashboard/stats")
def stats():
    one=lambda s: query(db(),s)[0]
    return {
      "total_threat_records":one("SELECT COUNT(*) n FROM threats")["n"],
      "critical_threats":one("SELECT COUNT(*) n FROM threats WHERE severity='CRITICAL'")["n"],
      "high_threats":one("SELECT COUNT(*) n FROM threats WHERE severity='HIGH'")["n"],
      "active_indicators":one("SELECT COUNT(*) n FROM indicators")["n"],
      "open_investigations":one("SELECT COUNT(*) n FROM alerts WHERE status IN ('NEW','INVESTIGATING')")["n"],
      "average_confidence":one("SELECT ROUND(AVG(confidence_score),1) n FROM threats")["n"],
      "vulnerabilities_tracked":one("SELECT COUNT(*) n FROM vulnerabilities")["n"]
    }

@api.get("/dashboard/trends")
def trends():
    return {"severity":query(db(),"SELECT severity,COUNT(*) count FROM threats GROUP BY severity ORDER BY count DESC"),
            "category":query(db(),"SELECT category,COUNT(*) count FROM threats GROUP BY category ORDER BY count DESC"),
            "indicator_type":query(db(),"SELECT indicator_type,COUNT(*) count FROM indicators GROUP BY indicator_type ORDER BY count DESC"),
            "tactics":query(db(),"SELECT tactic,COUNT(*) count FROM attack_mappings GROUP BY tactic ORDER BY count DESC")}

@api.get("/executive-summary")
def executive_summary():
    s=stats(); cats=query(db(),"SELECT category,COUNT(*) count FROM threats GROUP BY category ORDER BY count DESC LIMIT 5")
    vulns=query(db(),"SELECT product_category,COUNT(*) count FROM vulnerabilities GROUP BY product_category ORDER BY count DESC")
    return {"threat_landscape":s,"top_categories":cats,"vulnerability_categories":vulns,
            "recommended_priorities":["Review critical/high synthetic intelligence with authorized telemetry","Prioritize exposed critical assets","Strengthen awareness in low-scoring categories","Keep backups, MFA and patching controls current"]}

@api.get("/correlations")
def correlations():
    rows=query(db(),"SELECT t.threat_id,t.category AS threat_category,i.indicator_value FROM threats t JOIN indicators i ON t.threat_id=i.threat_id")
    from backend.services.correlation_engine import correlate_threats
    # Demo grouping uses stable synthetic campaign-like IDs derived from record suffix.
    for r in rows:
        r["campaign_id"]="CAMP-"+r["threat_id"][-2:]
        r["observation_window"]=r["threat_id"][:8]
    return correlate_threats(rows)

@api.get("/alerts")
def alerts(): return query(db(),"SELECT * FROM alerts ORDER BY timestamp DESC")
@api.put("/alerts/<alert_id>/status")
def alert_status(alert_id):
    body=request.get_json(silent=True) or {}
    status=body.get("status")
    allowed={"NEW","INVESTIGATING","MONITORING","RESOLVED","FALSE_POSITIVE"}
    if status not in allowed:return {"error":"Invalid status"},400
    execute(db(),"UPDATE alerts SET status=? WHERE alert_id=?",(status,alert_id))
    return {"updated":True,"alert_id":alert_id,"status":status}
@api.post("/threats/<threat_id>/notes")
def notes(threat_id):
    note=(request.get_json(silent=True) or {}).get("note","").strip()
    if not note:return {"error":"Note is required"},400
    execute(db(),"INSERT INTO analyst_notes(threat_id,note,created_at) VALUES(?,?,datetime('now'))",(threat_id,note))
    return {"saved":True},201
@api.get("/vulnerabilities")
def vulnerabilities(): return query(db(),"SELECT * FROM vulnerabilities ORDER BY priority_score DESC")
@api.get("/awareness/modules")
def modules():
    p=Path(__file__).resolve().parents[2]/"awareness/modules.json"
    return json.loads(p.read_text(encoding="utf-8"))
@api.get("/quiz")
def quiz():
    p=Path(__file__).resolve().parents[2]/"awareness/quiz_questions.json"
    return json.loads(p.read_text(encoding="utf-8"))
@api.post("/quiz/submit")
def quiz_submit():
    body=request.get_json(silent=True) or {}
    answers=body.get("answers",{})
    questions=json.loads((Path(__file__).resolve().parents[2]/"awareness/quiz_questions.json").read_text(encoding="utf-8"))
    correct=sum(1 for q in questions if str(answers.get(str(q["id"]),"")).upper()==q["correct"])
    score=round(correct/len(questions)*100)
    cats={}
    for q in questions:
        cat=q["category"]; cats.setdefault(cat,{"correct":0,"total":0}); cats[cat]["total"]+=1
        if str(answers.get(str(q["id"]),"")).upper()==q["correct"]:cats[cat]["correct"]+=1
    category_scores={k:round(v["correct"]/v["total"]*100) for k,v in cats.items()}
    weak=[k for k,v in category_scores.items() if v<61]
    return {"score":score,"category_scores":category_scores,"weakest_areas":weak,
            "recommendations":[f"Complete the {x} awareness module." for x in weak]}
