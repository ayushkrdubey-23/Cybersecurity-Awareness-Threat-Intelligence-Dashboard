# Conservative mapping: only map when the synthetic category has sufficient educational context.
MAPPINGS={
 "PHISHING":("Initial Access","Phishing","T1566"),
 "CREDENTIAL THREATS":("Credential Access","Valid Accounts","T1078"),
 "SOCIAL ENGINEERING":("Initial Access","Phishing","T1566"),
 "RANSOMWARE":("Impact","Data Encrypted for Impact","T1486"),
 "NETWORK THREATS":("Discovery","Network Service Scanning","T1046")
}
def map_category(category):
    item=MAPPINGS.get(category.upper())
    if not item: return None
    return {"tactic":item[0],"technique":item[1],"technique_id":item[2]}
