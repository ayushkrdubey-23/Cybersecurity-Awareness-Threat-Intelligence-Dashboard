import sqlite3, csv, json
from pathlib import Path
from backend.services.alert_engine import generate_threat_alert

SCHEMA="""
CREATE TABLE IF NOT EXISTS threats(threat_id TEXT PRIMARY KEY, threat_name TEXT, category TEXT, description TEXT, severity TEXT, risk_score INTEGER, confidence_score INTEGER, status TEXT, first_seen TEXT, last_seen TEXT);
CREATE TABLE IF NOT EXISTS indicators(indicator_id INTEGER PRIMARY KEY AUTOINCREMENT, threat_id TEXT, indicator_type TEXT, indicator_value TEXT, first_seen TEXT, last_seen TEXT);
CREATE TABLE IF NOT EXISTS sources(source_id INTEGER PRIMARY KEY AUTOINCREMENT, source_name TEXT, reliability TEXT);
CREATE TABLE IF NOT EXISTS attack_mappings(mapping_id INTEGER PRIMARY KEY AUTOINCREMENT, threat_id TEXT, tactic TEXT, technique TEXT, technique_id_optional TEXT);
CREATE TABLE IF NOT EXISTS vulnerabilities(vulnerability_id INTEGER PRIMARY KEY AUTOINCREMENT, cve_id TEXT, product_category TEXT, severity TEXT, cvss_score REAL, published_date TEXT, patch_available INTEGER, exploitation_status_demo TEXT, description TEXT, priority_score REAL);
CREATE TABLE IF NOT EXISTS alerts(alert_id TEXT PRIMARY KEY, threat_id TEXT, timestamp TEXT, alert_type TEXT, severity TEXT, risk_score INTEGER, confidence_score INTEGER, description TEXT, status TEXT);
CREATE TABLE IF NOT EXISTS analyst_notes(note_id INTEGER PRIMARY KEY AUTOINCREMENT, threat_id TEXT, note TEXT, created_at TEXT);
"""
def conn(path): return sqlite3.connect(path)
def init_db(path):
    with conn(path) as c: c.executescript(SCHEMA)
def seed_database(path):
    with conn(path) as c:
        if c.execute("SELECT COUNT(*) FROM threats").fetchone()[0]: return
        data_path=Path(__file__).resolve().parents[2]/"data"/"threat_intelligence_dataset.csv"
        with open(data_path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                c.execute("INSERT OR IGNORE INTO threats VALUES(?,?,?,?,?,?,?,?,?,?)",
                    (r["threat_id"],r["threat_name"],r["threat_category"],r["description"],r["severity"],int(r["risk_score"]),int(r["confidence_score"]),r["status"],r["first_seen"],r["last_seen"]))
                c.execute("INSERT INTO indicators(threat_id,indicator_type,indicator_value,first_seen,last_seen) VALUES(?,?,?,?,?)",
                    (r["threat_id"],r["indicator_type"],r["indicator_value"],r["first_seen"],r["last_seen"]))
                if r["mitre_tactic_optional"]:
                    c.execute("INSERT INTO attack_mappings(threat_id,tactic,technique,technique_id_optional) VALUES(?,?,?,?)",(r["threat_id"],r["mitre_tactic_optional"],r["mitre_technique_optional"],""))
                alert=generate_threat_alert(r)
                if alert:
                    c.execute("INSERT OR IGNORE INTO alerts VALUES(?,?,?,?,?,?,?,?,?)",tuple(alert.values()))
        sources=[("Internal SOC","A – Highly Reliable"),("Security Vendor","A – Highly Reliable"),("Public Threat Feed","B – Usually Reliable"),("Research Report","B – Usually Reliable"),("Community Submission","C – Fairly Reliable"),("Unknown Source","D – Reliability Unknown")]
        c.executemany("INSERT INTO sources(source_name,reliability) VALUES(?,?)",sources)
        vuln=Path(__file__).resolve().parents[2]/"data"/"vulnerabilities.csv"
        with open(vuln, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                c.execute("INSERT INTO vulnerabilities(cve_id,product_category,severity,cvss_score,published_date,patch_available,exploitation_status_demo,description,priority_score) VALUES(?,?,?,?,?,?,?,?,?)",
                    (r["cve_id"],r["product_category"],r["severity"],r["cvss_score"],r["published_date"],int(r["patch_available"]),r["exploitation_status_demo"],r["description"],r["priority_score"]))
def query(path,sql,args=()):
    with conn(path) as c:
        c.row_factory=sqlite3.Row
        return [dict(r) for r in c.execute(sql,args).fetchall()]
def execute(path,sql,args=()):
    with conn(path) as c:
        cur=c.execute(sql,args); c.commit(); return cur.lastrowid
