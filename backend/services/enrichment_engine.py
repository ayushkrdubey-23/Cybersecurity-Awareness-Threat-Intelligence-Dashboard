def enrich_indicator(indicator, rows, alerts=None):
    matches=[r for r in rows if r["indicator_value"].lower()==indicator.lower()]
    if not matches:
        return {"known":False,"indicator":indicator,"message":"No matching synthetic record found."}
    cats=sorted({r["threat_category"] for r in matches})
    return {"known":True,"indicator":indicator,"indicator_type":matches[0]["indicator_type"],
            "first_seen":min(r["first_seen"] for r in matches),"last_seen":max(r["last_seen"] for r in matches),
            "associated_categories":cats,"confidence":round(sum(r["confidence_score"] for r in matches)/len(matches)),
            "severity":max(matches,key=lambda x:x["risk_score"])["severity"],
            "risk_score":max(r["risk_score"] for r in matches),"related_alerts":alerts or [],
            "related_indicators":sorted({r["indicator_value"] for r in matches}),
            "mitre_mapping":[{"tactic":r["mitre_tactic_optional"],"technique":r["mitre_technique_optional"]} for r in matches if r["mitre_tactic_optional"]],
            "analyst_notes":"Synthetic enrichment only. Validate against authorized internal telemetry before action."}
