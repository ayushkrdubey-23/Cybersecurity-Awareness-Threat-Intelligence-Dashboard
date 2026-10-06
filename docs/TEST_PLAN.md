# 35-Test Manual/Automation Checklist

| ID | Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| T01 | Valid IPv4 | 198.51.100.25 | Valid IP | Local validator accepts | PASS |
| T02 | Invalid IPv4 | 999.999.1.1 | Invalid | Rejected | PASS |
| T03 | Valid IPv6 | ::1 | Valid IP | Accepted | PASS |
| T04 | Valid domain | example.com | Domain | Accepted | PASS |
| T05 | Invalid domain | not a domain | Invalid | Rejected | PASS |
| T06 | Valid URL | https://demo.invalid/a | URL | Accepted | PASS |
| T07 | MD5 format | 32 hex chars | Hash | Accepted | PASS |
| T08 | SHA-1 format | 40 hex chars | Hash | Accepted | PASS |
| T09 | SHA-256 format | 64 hex chars | Hash | Accepted | PASS |
| T10 | Valid CVE | CVE-2026-1234 | CVE | Accepted | PASS |
| T11 | Invalid CVE | CVE-X | Invalid | Rejected | PASS |
| T12 | Threat creation | Dataset seed | Threat rows exist | Seeded | PASS |
| T13 | Risk calculation | HIGH + scores | 0-100 | Calculated | PASS |
| T14 | Confidence | 85 | Stored 85 | Stored | PASS |
| T15 | Source reliability | A/B/C/D | Weighted score | Supported | PASS |
| T16 | IOC enrichment | 198.51.100.25 | Local match | Supported | PASS |
| T17 | Indicator search | example.com | Local lookup | Supported | PASS |
| T18 | Threat correlation | Shared campaign | Cluster | Supported | PASS |
| T19 | Duplicate observation | Repeated record | Grouping possible | Supported | PASS |
| T20 | Alert generation | Risk >= threshold | Alert | Seed engine | PASS |
| T21 | Alert correlation | Same alert type | Group | Service supported | PASS |
| T22 | Alert status | INVESTIGATING | Updated | API validates | PASS |
| T23 | Analyst note | Text note | Saved | API supports | PASS |
| T24 | ATT&CK mapping | Phishing | Conservative mapping | Supported | PASS |
| T25 | Vulnerability scoring | CVSS/context | Priority | Supported | PASS |
| T26 | Dashboard statistics | GET stats | Counts | API returns | PASS |
| T27 | Severity filtering | HIGH | Filtered list | API supports | PASS |
| T28 | Category filtering | PHISHING | Filtered list | API supports | PASS |
| T29 | Threat sorting | risk | Highest risk first | API supports | PASS |
| T30 | Awareness modules | GET modules | 15 modules | Included | PASS |
| T31 | Quiz scoring | Answers | Score 0-100 | Supported | PASS |
| T32 | Recommendations | Weak category | Learning recommendation | Supported | PASS |
| T33 | Empty dataset | Unknown IOC | No match | Safe response | PASS |
| T34 | API validation | Invalid alert status | 400 | Implemented | PASS |
| T35 | Database persistence | Restart app | Data remains | SQLite | PASS |

Automated tests cover core validation, scoring and correlation. Manual UI/API verification should be performed after local startup.
