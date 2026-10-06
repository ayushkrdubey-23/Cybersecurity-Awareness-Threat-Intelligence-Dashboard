def correlate_threats(records):
    clusters={}
    for r in records:
        key=(r.get("campaign_id",""), r.get("threat_category",""), r.get("observation_window",""))
        if key[0]:
            clusters.setdefault(key, []).append(r.get("indicator_value"))
    return [{"cluster_id":f"CL-{i:03d}","indicators":sorted(set(vals)),"evidence":"Shared synthetic campaign/category/window"} for i,vals in enumerate(clusters.values(),1) if len(vals)>1]

def correlate_alerts(alerts):
    groups={}
    for a in alerts:
        groups.setdefault((a.get("threat_id"),a.get("alert_type")),[]).append(a)
    return [{"threat_id":k[0],"alert_type":k[1],"observation_count":len(v),"correlated":len(v)>1} for k,v in groups.items()]
