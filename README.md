# Cybersecurity Awareness & Threat Intelligence Dashboard

## Overview
A defensive, industry-oriented student project combining synthetic cyber threat intelligence, IOC validation, enrichment, risk/confidence scoring, vulnerability awareness, alert workflows, MITRE ATT&CK-oriented mapping, SOC investigation, and cybersecurity awareness training.

## Safety
This project uses synthetic/demo indicators and local database lookups. It does **not** execute malware, visit suspicious URLs, scan external systems, exploit vulnerabilities, or contact suspicious IPs/domains.

## Objectives
- Analyze IOCs as data.
- Distinguish observations, indicators, alerts, threats and incidents.
- Demonstrate SOC-style workflows.
- Teach practical security awareness.
- Provide reproducible GitHub proof of work.

## Features
- 2,000 synthetic threat records.
- IP/domain/URL/hash/CVE validation.
- Local IOC search and enrichment.
- Risk score from severity, confidence, recency, observations, source reliability and context.
- Confidence scoring.
- Source reliability model.
- Threat correlation and alert correlation concepts.
- Conservative MITRE ATT&CK mapping.
- Synthetic vulnerability prioritization.
- SOC dashboard and investigation view.
- 15 awareness modules.
- 30-question awareness quiz and recommendations.
- Executive summary API.
- Automated unit tests.

## Architecture
Synthetic/Public Defensive Data → Ingestion → Normalization → IOC Validation → Enrichment → Risk + Confidence → Correlation → Threat DB / Alerts / ATT&CK → SOC Dashboard → Analyst.

Awareness Content → Learning Modules → Quiz → Awareness Score → Recommendations.

## Technology Stack
Python, Flask, SQLite, Pandas, HTML, CSS, JavaScript, Chart-ready API data, pytest.

## Project Structure
```text
backend/       Flask API and security-analysis services
frontend/      Static dashboard pages
awareness/     Learning modules and quiz data
data/          Dataset and generators
tests/         Automated tests
docs/          Project documentation
reports/       Report material
screenshots/   Evidence screenshots
```

## Risk vs Confidence
Risk asks how concerning an event may be. Confidence asks how strong the available evidence is. A high-risk, low-confidence item requires validation rather than automatic escalation.

## IOC Limitation
IOC match ≠ confirmed compromise. Indicators can become stale, be shared by benign infrastructure, or lack context.

## API
- `GET /api/health`
- `GET /api/threats`
- `GET /api/threats/{id}`
- `GET /api/indicators/search?q=...`
- `GET /api/dashboard/stats`
- `GET /api/dashboard/trends`
- `GET /api/alerts`
- `PUT /api/alerts/{id}/status`
- `POST /api/threats/{id}/notes`
- `GET /api/vulnerabilities`
- `GET /api/awareness/modules`
- `GET /api/quiz`
- `POST /api/quiz/submit`
- `GET /api/executive-summary`
- `GET /api/correlations`

Swagger/OpenAPI is not required for this beginner Flask implementation; API behavior is documented in `docs/API.md`.

## Local Installation
See `docs/RUN_GUIDE.md`.

## Testing
Run `pytest -q`. The project includes automated tests for indicator formats, scoring, correlation and defensive boundaries. A complete manual test catalog is in `docs/TEST_PLAN.md`.

## GitHub
Suggested repository name: `Cybersecurity-Awareness-Threat-Intelligence-Dashboard`

Suggested topics:
`cybersecurity`, `threat-intelligence`, `cti`, `soc`, `ioc`, `mitre-attack`, `security-awareness`, `python`, `flask`, `fastapi`, `vulnerability-management`, `incident-response`, `security-analytics`, `defensive-security`

## Ethical Disclaimer
This project is designed exclusively for defensive cybersecurity education, threat-intelligence analysis, and security awareness. It does not execute, deploy, or interact with malicious payloads or unauthorized systems.

## Author
Ayush Kumar Dubey
