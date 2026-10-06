SEVERITY_SCORE={"INFORMATIONAL":10,"LOW":30,"MEDIUM":50,"HIGH":75,"CRITICAL":95}
SOURCE_RELIABILITY={"A – Highly Reliable":100,"B – Usually Reliable":85,"C – Fairly Reliable":65,"D – Reliability Unknown":40}

def calculate_threat_risk(severity, confidence, recency, observations, source_reliability, context):
    severity_component=SEVERITY_SCORE.get(severity.upper(),50)
    observation=min(100, observations*10)
    values=[severity_component, float(confidence), float(recency), observation, float(source_reliability), float(context)]
    return round(values[0]*.30+values[1]*.25+values[2]*.15+values[3]*.10+values[4]*.10+values[5]*.10)

def classify_risk(score):
    if score <= 20: return "INFORMATIONAL"
    if score <= 40: return "LOW"
    if score <= 60: return "MEDIUM"
    if score <= 80: return "HIGH"
    return "CRITICAL"

def calculate_vulnerability_priority(cvss, asset_criticality, exposure, exploitation_evidence, business_context):
    return round(min(100, cvss*.5 + asset_criticality*.15 + exposure*.15 + exploitation_evidence*.1 + business_context*.1), 2)
