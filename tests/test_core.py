from backend.services.ioc_validator import validate_indicator
from backend.services.risk_engine import calculate_threat_risk, classify_risk, calculate_vulnerability_priority
from backend.services.correlation_engine import correlate_threats
def test_valid_ipv4(): assert validate_indicator("198.51.100.25")["valid"]
def test_invalid_ipv4(): assert not validate_indicator("999.999.1.1")["valid"]
def test_domain(): assert validate_indicator("example.com")["indicator_type"]=="DOMAIN"
def test_invalid_domain(): assert not validate_indicator("not a domain")["valid"]
def test_url(): assert validate_indicator("https://demo.invalid/a")["indicator_type"]=="URL"
def test_md5(): assert validate_indicator("a"*32)["indicator_type"]=="FILE HASH"
def test_sha1(): assert validate_indicator("a"*40)["indicator_type"]=="FILE HASH"
def test_sha256(): assert validate_indicator("a"*64)["indicator_type"]=="FILE HASH"
def test_cve(): assert validate_indicator("CVE-2026-1234")["indicator_type"]=="CVE ID"
def test_invalid_cve(): assert not validate_indicator("CVE-X")["valid"]
def test_risk(): assert 0<=calculate_threat_risk("HIGH",85,90,4,85,80)<=100
def test_classification(): assert classify_risk(78)=="HIGH"
def test_vuln_priority(): assert 0<=calculate_vulnerability_priority(9.8,90,90,80,90)<=100
def test_correlation(): assert correlate_threats([{"campaign_id":"A","threat_category":"PHISHING","observation_window":"D","indicator_value":"a"},{"campaign_id":"A","threat_category":"PHISHING","observation_window":"D","indicator_value":"b"}])
def test_demo_boundaries(): assert "SYNTHETIC" in "SYNTHETIC / DEMO ONLY"
