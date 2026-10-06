import ipaddress, re
from urllib.parse import urlparse

DOMAIN_RE = re.compile(r"^(?=.{1,253}$)(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+(?:[A-Za-z]{2,63}|invalid)$")
CVE_RE = re.compile(r"^CVE-\d{4}-\d{4,}$")
HASH_PATTERNS = {32:"MD5", 40:"SHA-1", 64:"SHA-256"}

def validate_indicator(value):
    raw = (value or "").strip()
    if not raw:
        return {"valid": False, "indicator_type": None, "normalized_value": "", "validation_notes": "Value is empty."}
    try:
        ip = ipaddress.ip_address(raw)
        return {"valid": True, "indicator_type": "IP ADDRESS", "normalized_value": str(ip), "validation_notes": "Syntactically valid IP; this does not indicate maliciousness."}
    except ValueError:
        pass
    if CVE_RE.fullmatch(raw.upper()):
        return {"valid": True, "indicator_type": "CVE ID", "normalized_value": raw.upper(), "validation_notes": "Syntactically valid CVE identifier."}
    if len(raw) in HASH_PATTERNS and re.fullmatch(r"[0-9a-fA-F]+", raw):
        return {"valid": True, "indicator_type": "FILE HASH", "normalized_value": raw.lower(), "validation_notes": f"Syntactically valid {HASH_PATTERNS[len(raw)]}-format hash."}
    parsed = urlparse(raw)
    if parsed.scheme in {"http","https"} and parsed.netloc:
        return {"valid": True, "indicator_type": "URL", "normalized_value": raw, "validation_notes": "Syntactically valid URL; the application will not contact it."}
    domain = raw.lower().rstrip(".")
    if DOMAIN_RE.fullmatch(domain):
        return {"valid": True, "indicator_type": "DOMAIN", "normalized_value": domain, "validation_notes": "Syntactically valid domain; the application performs database lookup only."}
    return {"valid": False, "indicator_type": "UNKNOWN", "normalized_value": domain, "validation_notes": "Format not recognized by the local validator."}
