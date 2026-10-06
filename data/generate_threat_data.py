import csv, random, hashlib
from datetime import datetime, timedelta
from pathlib import Path
random.seed(2026)
BASE=Path(__file__).resolve().parent
CATS=["PHISHING","MALWARE","RANSOMWARE","CREDENTIAL THREATS","WEB THREATS","NETWORK THREATS","VULNERABILITY EXPOSURE","SOCIAL ENGINEERING","DATA EXPOSURE","ACCOUNT SECURITY"]
TYPES=["IP ADDRESS","DOMAIN","URL","FILE HASH","EMAIL/SENDER DOMAIN","CVE ID"]
SEVS=["INFORMATIONAL","LOW","MEDIUM","HIGH","CRITICAL"]
SOURCES=["Internal SOC","Security Vendor","Public Threat Feed","Research Report","Community Submission","Unknown Source"]
STATUS=["NEW","UNDER_REVIEW","MONITORING","CLOSED","FALSE_POSITIVE"]
TACTICS=["Initial Access","Credential Access","Impact","Discovery","Persistence","Command and Control","Exfiltration",""]
TECH={"Initial Access":"Phishing","Credential Access":"Valid Accounts","Impact":"Data Encrypted for Impact","Discovery":"Network Service Scanning","Persistence":"Account Access Removal","Command and Control":"Application Layer Protocol","Exfiltration":"Exfiltration Over Web Service","":" "}
def indicator(i,t):
    if t=="IP ADDRESS": return f"{random.choice(['192.0.2','198.51.100','203.0.113'])}.{i%254+1}"
    if t=="DOMAIN": return random.choice(["example.com","example.org","example.net","demo.invalid"])
    if t=="URL": return f"https://demo.invalid/threat/{i}"
    if t=="FILE HASH": return hashlib.sha256(f"synthetic-{i}".encode()).hexdigest()
    if t=="EMAIL/SENDER DOMAIN": return random.choice(["mail.example.org","alerts.example.net"])
    return f"CVE-2026-{1000+i%9000:04d}"
rows=[]
start=datetime(2026,1,1)
for i in range(1,2001):
    cat=random.choice(CATS); typ=random.choice(TYPES); sev=random.choices(SEVS,weights=[5,20,35,28,12])[0]
    conf=random.randint(45,98); rec=random.randint(35,100); obs=random.randint(1,10); src_rel=random.choice([40,65,85,100]); ctx=random.randint(30,100)
    sevscore={"INFORMATIONAL":10,"LOW":30,"MEDIUM":50,"HIGH":75,"CRITICAL":95}[sev]
    risk=round(sevscore*.30+conf*.25+rec*.15+min(100,obs*10)*.10+src_rel*.10+ctx*.10)
    first=start+timedelta(days=random.randint(0,280)); last=first+timedelta(days=random.randint(0,30))
    tactic=random.choice(TACTICS); technique=TECH[tactic]
    rows.append({"threat_id":f"THR-2026-{i:04d}","timestamp":last.isoformat(),"threat_name":f"Synthetic {cat.title()} Observation {i}","threat_category":cat,"indicator_type":typ,"indicator_value":indicator(i,typ),"source_name":random.choice(SOURCES),"confidence_score":conf,"severity":sev,"risk_score":risk,"status":random.choice(STATUS),"first_seen":first.date().isoformat(),"last_seen":last.date().isoformat(),"country_or_region_optional":random.choice(["IN","US","EU","Global","Demo"]), "description":"SYNTHETIC / DEMO ONLY. This record is safe educational data and is not evidence of a real attack.","mitre_tactic_optional":tactic,"mitre_technique_optional":technique,"cve_id_optional":f"CVE-2026-{1000+i%9000:04d}" if typ=="CVE ID" else "", "campaign_id":f"CAMP-{i%40:02d}","observation_window":first.strftime("%Y-%m-%d")})
# required file contains requested public schema plus internal grouping fields
fields=["threat_id","timestamp","threat_name","threat_category","indicator_type","indicator_value","source_name","confidence_score","severity","risk_score","status","first_seen","last_seen","country_or_region_optional","description","mitre_tactic_optional","mitre_technique_optional","cve_id_optional","campaign_id","observation_window"]
with open(BASE/"threat_intelligence_dataset.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
print(f"Generated {len(rows)} synthetic records.")
