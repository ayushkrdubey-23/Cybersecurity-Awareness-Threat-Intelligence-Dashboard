# Cybersecurity Awareness & Threat Intelligence Dashboard

A defensive, industry-oriented cybersecurity project that combines **Cyber Threat Intelligence (CTI)**, **IOC analysis**, **risk and confidence scoring**, **correlation**, **SOC-style alert handling**, **MITRE ATT&CK-oriented mapping**, **vulnerability awareness**, and **cybersecurity awareness training** in one beginner-friendly application.

> **Project type:** Defensive cybersecurity / Threat Intelligence / SOC awareness / Security analytics
>
> **Data policy:** Synthetic and public-safe demonstration data only
>
> **Primary purpose:** Education, portfolio development, security analytics practice, and GitHub-ready proof of work

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Objectives](#objectives)
3. [Key Features](#key-features)
4. [Why This Project Matters](#why-this-project-matters)
5. [System Architecture](#system-architecture)
6. [Technology Stack](#technology-stack)
7. [Project Structure](#project-structure)
8. [Data and Synthetic Threat Intelligence](#data-and-synthetic-threat-intelligence)
9. [Threat Intelligence Workflow](#threat-intelligence-workflow)
10. [IOC Analysis](#ioc-analysis)
11. [Risk and Confidence Scoring](#risk-and-confidence-scoring)
12. [Correlation and Alert Management](#correlation-and-alert-management)
13. [MITRE ATT&CK Mapping](#mitre-attck-mapping)
14. [Vulnerability Awareness](#vulnerability-awareness)
15. [Cybersecurity Awareness Module](#cybersecurity-awareness-module)
16. [Quiz and Recommendations](#quiz-and-recommendations)
17. [Executive Summary](#executive-summary)
18. [API Endpoints](#api-endpoints)
19. [Installation on Windows / VS Code](#installation-on-windows--vs-code)
20. [Running the Project](#running-the-project)
21. [Testing](#testing)
22. [Safety and Ethical Boundaries](#safety-and-ethical-boundaries)
23. [Limitations](#limitations)
24. [GitHub Strategy](#github-strategy)
25. [Future Enhancements](#future-enhancements)
26. [Author](#author)

---

## Project Overview

The **Cybersecurity Awareness & Threat Intelligence Dashboard** demonstrates how a security analyst can organize threat-intelligence information into a practical defensive workflow.

The project accepts synthetic threat records and processes them through a sequence of validation, normalization, enrichment, scoring, correlation, alerting, and analyst-facing visualization steps. It also includes a cybersecurity awareness area containing learning modules and a quiz so that technical threat analysis is connected with human security awareness.

The project intentionally avoids active interaction with suspicious infrastructure. Threat indicators are treated as **data**, not as targets for network activity.

---

## Objectives

The major objectives are to:

- Analyze Indicators of Compromise (IOCs) as structured data.
- Validate common IOC types such as IP addresses, domains, URLs, hashes, and CVE-style identifiers.
- Normalize threat-intelligence records for consistent analysis.
- Add local, safe enrichment information to indicators.
- Calculate a defensive **risk score** and an evidence-based **confidence score**.
- Correlate related threat observations.
- Demonstrate a SOC-style alert lifecycle.
- Associate selected threat behavior with MITRE ATT&CK-oriented techniques.
- Provide vulnerability-awareness and prioritization information using synthetic data.
- Teach practical cybersecurity awareness concepts.
- Provide a quiz and recommendations for improving awareness.
- Produce an executive-level security summary.
- Maintain a reproducible, GitHub-ready project structure.

---

## Key Features

### Threat Intelligence

- 2,000 synthetic threat-intelligence records.
- Structured fields for threat category, severity, confidence, source, IOC type, IOC value, timestamps, observations, context, and status.
- Local dataset generation for reproducible demonstrations.

### IOC Analysis

- IP validation.
- Domain validation.
- URL validation.
- Hash validation.
- CVE-style identifier validation.
- IOC search from the local dataset.
- Defensive interpretation of IOC matches.

### Enrichment

- Local enrichment without contacting suspicious or external infrastructure.
- Source information and contextual metadata.
- Reputation-style information derived from demonstration data.
- Recency and observation context.

### Risk and Confidence

- Risk scoring using multiple defensive factors.
- Confidence scoring to indicate evidence strength.
- Severity and source-reliability considerations.
- Recency and observation/context considerations.
- Explicit distinction between **risk** and **confidence**.

### Correlation and Alerts

- Threat correlation using shared/contextual attributes.
- Alert generation from risk-oriented conditions.
- SOC-style alert status handling.
- Investigation notes for analyst workflow.

### MITRE ATT&CK Orientation

- Conservative behavior-to-technique mapping.
- Mapping is presented as an analytical aid, not as proof that an attack occurred.

### Vulnerability Awareness

- Synthetic vulnerability records.
- Severity and priority information.
- Defensive vulnerability-awareness workflow.

### Security Awareness

- 15 awareness modules.
- 30-question cybersecurity awareness quiz.
- Quiz scoring.
- Improvement recommendations.

### Dashboard and Reporting

- SOC-style dashboard.
- Threat detail view.
- Awareness learning area.
- Quiz page.
- Executive summary API.
- Testing and documentation materials.

---

## Why This Project Matters

Real security operations generate large numbers of observations, indicators, alerts, and contextual events. Analysts therefore need ways to:

1. Validate and normalize information.
2. Separate weak evidence from stronger evidence.
3. Prioritize potentially important events.
4. Correlate related observations.
5. Document analyst decisions.
6. Communicate useful results to technical and non-technical stakeholders.

This project demonstrates those ideas through a safe, reproducible educational implementation.

---

## System Architecture

```text
                  Synthetic / Public-Safe Data
                              |
                              v
                     Data Ingestion Layer
                              |
                              v
                       Normalization
                              |
                              v
                        IOC Validation
                              |
                              v
                         Enrichment
                              |
                    +---------+---------+
                    |                   |
                    v                   v
              Risk Scoring       Confidence Scoring
                    |                   |
                    +---------+---------+
                              |
                              v
                         Correlation
                              |
                    +---------+---------+
                    |                   |
                    v                   v
                  Alerts        Threat / IOC Database
                    |                   |
                    +---------+---------+
                              |
                              v
                   MITRE ATT&CK Mapping
                              |
                              v
                         SOC Dashboard
                              |
                +-------------+-------------+
                |                           |
                v                           v
        Analyst Investigation       Executive Summary

      Awareness Content -> Learning Modules -> Quiz
                                      |
                                      v
                             Score + Recommendations
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Backend | Python, Flask |
| API | Flask REST-style JSON endpoints |
| Database | SQLite |
| Data Processing | Pandas |
| Frontend | HTML, CSS, JavaScript |
| Testing | Pytest |
| Configuration | python-dotenv |
| Cross-Origin Support | Flask-CORS |
| Development IDE | Visual Studio Code |
| Environment | Python virtual environment (`.venv`) |

---

## Project Structure

```text
Cybersecurity-Awareness-Threat-Intelligence-Dashboard/
│
├── backend/
│   ├── app.py
│   ├── models/
│   ├── routes/
│   │   └── api.py
│   ├── services/
│   │   ├── ioc_validator.py
│   │   ├── enrichment_engine.py
│   │   ├── risk_engine.py
│   │   ├── correlation_engine.py
│   │   ├── alert_engine.py
│   │   ├── attack_mapper.py
│   │   └── database.py
│   └── utils/
│
├── frontend/
│   ├── index.html
│   ├── threat-dashboard.html
│   ├── threat-details.html
│   ├── awareness.html
│   ├── quiz.html
│   ├── css/
│   │   └── style.css
│   └── js/
│
├── awareness/
│   ├── modules.json
│   └── quiz_questions.json
│
├── data/
│   ├── generate_threat_data.py
│   ├── threat_intelligence_dataset.csv
│   └── vulnerabilities.csv
│
├── tests/
│   └── test_core.py
│
├── screenshots/
│
├── reports/
│   └── TEST_RESULTS.md
│
├── docs/
│   ├── RUN_GUIDE.md
│   ├── API.md
│   ├── TEST_PLAN.md
│   ├── PROJECT_REPORT.md
│   ├── GITHUB_STRATEGY.md
│   ├── SCREENSHOT_CHECKLIST.md
│   └── ATTACHED_SPECIFICATION.txt
│
├── .env.example
├── .gitignore
├── requirements.txt
├── RUN_PROJECT.txt
└── README.md
```

---

## Data and Synthetic Threat Intelligence

The project includes a **2,000-record synthetic threat-intelligence dataset** for demonstration and testing.

The dataset is designed to resemble structured CTI records without representing real malicious infrastructure.

Typical information includes:

- Threat identifier.
- Timestamp.
- Threat category.
- IOC type.
- IOC value.
- Severity.
- Confidence.
- Source.
- Source reliability.
- Observation count.
- Context.
- Status.
- Related analytical metadata.

The generator is located at:

```text
 data/generate_threat_data.py
```

To regenerate the dataset:

```powershell
python data\generate_threat_data.py
```

The generated file is:

```text
data\threat_intelligence_dataset.csv
```

---

## Threat Intelligence Workflow

The analytical workflow follows this sequence:

```text
Input Record
    |
    v
Normalize Fields
    |
    v
Validate IOC
    |
    v
Local Enrichment
    |
    v
Calculate Risk
    |
    v
Calculate Confidence
    |
    v
Correlate Related Events
    |
    v
Generate / Update Alert
    |
    v
Map Relevant ATT&CK Technique
    |
    v
Analyst Investigation
    |
    v
Executive / Dashboard Reporting
```

This separation helps demonstrate the difference between collecting information and making a security decision from that information.

---

## IOC Analysis

The project supports safe analysis of common IOC categories:

| IOC Type | Example format | Defensive purpose |
|---|---|---|
| IP | `198.51.100.25` | Identify and classify an IP indicator |
| Domain | `example.invalid` | Validate and search domain indicators |
| URL | `https://demo.invalid/path` | Validate URL structure without visiting it |
| Hash | Synthetic MD5/SHA-style value | Validate hash format |
| CVE | `CVE-2026-1234` | Recognize vulnerability-style identifiers |

The project intentionally uses documentation/test domains and reserved IP ranges where applicable.

### Important IOC Principle

> **IOC match does not equal confirmed compromise.**

An indicator can be stale, shared by legitimate infrastructure, incomplete, incorrectly attributed, or lacking sufficient context. Therefore, a match should be treated as an analytical signal that requires validation.

---

## Risk and Confidence Scoring

The project deliberately keeps **risk** and **confidence** separate.

### Risk

Risk represents how concerning an event or threat observation may be.

A higher risk score can be influenced by factors such as:

- Severity.
- Observation count.
- Recency.
- Context.
- Source reliability.
- Other analytical signals.

### Confidence

Confidence represents how strongly the available evidence supports the analytical conclusion.

A high-confidence result means the evidence is stronger or more consistent. It does not automatically mean the activity is malicious.

### Risk vs Confidence Matrix

| Risk | Confidence | Suggested interpretation |
|---|---|---|
| High | High | Strong candidate for analyst attention |
| High | Low | Important signal, but validate before escalation |
| Low | High | Well-supported but currently low concern |
| Low | Low | Weak signal; monitor or collect more context |

A particularly important security-analytics principle demonstrated here is:

> **High risk with low confidence should trigger validation, not blind escalation.**

---

## Correlation and Alert Management

Threat correlation groups related observations using available structured attributes and context.

Examples of correlation ideas include:

- Shared IOC values.
- Related threat categories.
- Similar sources.
- Similar timestamps or activity windows.
- Repeated observations.
- Common contextual attributes.

The alert workflow provides a simple SOC-style lifecycle so an analyst can review alerts and update their status.

Possible actions include:

```text
New Alert
   |
   v
Analyst Review
   |
   +----> Needs Validation
   |
   +----> Escalated
   |
   +----> Resolved
```

Investigation notes can be stored against threat records to document analyst reasoning.

---

## MITRE ATT&CK Mapping

The project includes **conservative MITRE ATT&CK-oriented mapping** for selected behavior categories.

The mapping should be interpreted as:

```text
Observed / represented behavior
            |
            v
Possible ATT&CK technique association
            |
            v
Analyst validation
```

The presence of a mapping does **not** prove that a real attack, adversary, or compromise occurred.

---

## Vulnerability Awareness

The vulnerability-awareness module uses synthetic vulnerability records to demonstrate defensive prioritization.

The workflow is intended to show how security teams can organize vulnerability information using factors such as:

- Severity.
- Priority.
- Affected context.
- Remediation urgency.

This is an awareness and prioritization workflow; the project does not exploit vulnerabilities or test unauthorized systems.

---

## Cybersecurity Awareness Module

The project also addresses the human side of cybersecurity.

The awareness section includes **15 learning modules** covering practical defensive concepts such as:

- Password and authentication hygiene.
- Phishing awareness.
- Safe browsing.
- Social engineering awareness.
- Malware awareness.
- Secure device usage.
- Data protection.
- Incident reporting.
- Privacy and account security.

The exact module content is stored in:

```text
awareness/modules.json
```

---

## Quiz and Recommendations

The application includes a **30-question cybersecurity awareness quiz**.

Quiz content is stored in:

```text
awareness/quiz_questions.json
```

The quiz workflow is:

```text
Answer Questions
       |
       v
Calculate Score
       |
       v
Determine Awareness Level
       |
       v
Generate Recommendations
```

The goal is to convert awareness training into an interactive assessment rather than providing only static documentation.

---

## Executive Summary

The executive-summary endpoint provides a high-level representation of the threat environment for non-technical stakeholders.

An executive view should focus on:

- Overall threat volume.
- Severity distribution.
- Alert trends.
- Major categories.
- Risk concentration.
- Recommended defensive attention areas.

This separates analyst-level investigation from management-level communication.

---

## API Endpoints

The backend exposes the following endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/health` | API health check |
| GET | `/api/threats` | List threat records |
| GET | `/api/threats/{id}` | Get a threat record by ID |
| GET | `/api/indicators/search?q=...` | Search local IOC data |
| GET | `/api/dashboard/stats` | Dashboard statistics |
| GET | `/api/dashboard/trends` | Trend information |
| GET | `/api/alerts` | Retrieve alerts |
| PUT | `/api/alerts/{id}/status` | Update an alert status |
| POST | `/api/threats/{id}/notes` | Add investigation notes |
| GET | `/api/vulnerabilities` | Retrieve vulnerability-awareness data |
| GET | `/api/awareness/modules` | Retrieve awareness modules |
| GET | `/api/quiz` | Retrieve quiz questions |
| POST | `/api/quiz/submit` | Submit quiz answers |
| GET | `/api/executive-summary` | Executive security summary |
| GET | `/api/correlations` | Correlated threat information |

Detailed API information is available in:

```text
docs/API.md
```

This project uses a beginner-friendly Flask API implementation. Swagger/OpenAPI tooling is not required for the current version.

---

## Installation on Windows / VS Code

### 1. Open the project

Extract the project ZIP and open the project folder in **Visual Studio Code**.

Open:

```text
Cybersecurity-Awareness-Threat-Intelligence-Dashboard
```

### 2. Open the VS Code terminal

Use:

```text
Terminal -> New Terminal
```

### 3. Create a virtual environment

```powershell
py -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for the current terminal session, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Upgrade pip

Because some Windows security policies can block `pip.exe`, the recommended command is:

```powershell
python -m pip install --upgrade pip
```

### 6. Install project dependencies

Use Python to invoke pip:

```powershell
python -m pip install -r requirements.txt
```

Do **not** rely on the standalone `pip` command when Windows Application Control blocks `pip.exe`.

### 7. Generate the dataset

```powershell
python data\generate_threat_data.py
```

---

## Running the Project

The project uses two local development servers: one for the Flask backend and one for the static frontend.

### Terminal 1 — Start the Backend

At the project root:

```powershell
python -m backend.app
```

Backend URL:

```text
http://127.0.0.1:8000
```

Keep this terminal running.

### Terminal 2 — Start the Frontend

Open another VS Code terminal.

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Move into the frontend folder:

```powershell
cd frontend
```

Start the static server:

```powershell
python -m http.server 5500
```

Frontend URL:

```text
http://127.0.0.1:5500
```

### Main Pages

Dashboard:

```text
http://127.0.0.1:5500/
```

Threat details:

```text
http://127.0.0.1:5500/threat-details.html
```

Awareness modules:

```text
http://127.0.0.1:5500/awareness.html
```

Quiz:

```text
http://127.0.0.1:5500/quiz.html
```

---

## API Verification from PowerShell

With the backend running, open another terminal and run:

### Health Check

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/health
```

### Dashboard Statistics

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/dashboard/stats
```

### IOC Search

Example using a documentation-range IP from the synthetic dataset:

```powershell
Invoke-RestMethod "http://127.0.0.1:8000/api/indicators/search?q=198.51.100.25"
```

### Vulnerabilities

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/vulnerabilities
```

### Executive Summary

```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/executive-summary
```

---

## Testing

The project includes automated tests in:

```text
tests/test_core.py
```

Run the tests from the project root:

```powershell
python -m pytest -q
```

Also compile-check the backend source:

```powershell
python -m compileall backend
```

The project includes tests covering defensive core logic such as:

- IOC format validation.
- Risk calculation.
- Confidence-related behavior.
- Correlation functionality.
- Defensive safety boundaries.

A broader manual validation checklist is available at:

```text
docs/TEST_PLAN.md
```

Test-result documentation is available at:

```text
reports/TEST_RESULTS.md
```

---

## Safety and Ethical Boundaries

This project is intentionally designed for **defensive cybersecurity education**.

### The project does NOT

- Execute malware.
- Deploy malicious payloads.
- Visit suspicious URLs.
- Contact suspicious IP addresses or domains.
- Scan external systems.
- Exploit vulnerabilities.
- Perform unauthorized reconnaissance.
- Attempt credential theft.
- Collect real user passwords or private credentials.
- Interact with malicious infrastructure.

### The project DOES

- Analyze synthetic indicators as data.
- Validate IOC formats.
- Perform local enrichment from safe datasets.
- Demonstrate risk and confidence concepts.
- Correlate threat observations.
- Demonstrate alert workflows.
- Provide awareness education.
- Support defensive SOC-style analysis.

The correct interpretation of this project is therefore **simulation and defensive analysis**, not offensive operation.

---

## Limitations

This is an educational and portfolio-oriented implementation rather than a production CTI/SOC platform.

Important limitations include:

- Threat data is synthetic and is not a live intelligence feed.
- Enrichment is local/demo-oriented rather than live external reputation lookup.
- Risk scoring is a demonstration model and should not be treated as a production decision engine.
- MITRE ATT&CK associations are analytical mappings, not incident attribution.
- IOC matches do not prove compromise.
- SQLite is appropriate for this educational implementation but may not be the right choice for high-scale production workloads.
- The frontend is a static development frontend rather than a hardened production deployment.

---

## GitHub Strategy

Suggested repository name:

```text
Cybersecurity-Awareness-Threat-Intelligence-Dashboard
```

Suggested description:

```text
Defensive cybersecurity dashboard for synthetic threat intelligence, IOC analysis, risk scoring, alert correlation, MITRE ATT&CK mapping, vulnerability awareness, and security awareness training.
```

Suggested GitHub topics:

```text
cybersecurity
threat-intelligence
cti
soc
ioc
mitre-attack
security-awareness
python
flask
vulnerability-management
incident-response
security-analytics
defensive-security

```

A staged commit approach is documented in:

```text
docs/GITHUB_STRATEGY.md
```

This helps maintain a traceable development history and makes project progress easier to review.

---

## Documentation Included

### Run Guide

```text
docs/RUN_GUIDE.md
```

Detailed Windows/PowerShell/VS Code setup and startup instructions.

### API Documentation

```text
docs/API.md
```

Endpoint-level API documentation.

### Test Plan

```text
docs/TEST_PLAN.md
```

Manual and automated verification checklist.

### Project Report

```text
docs/PROJECT_REPORT.md
```

Long-form project explanation suitable for academic/project documentation.

### GitHub Strategy

```text
docs/GITHUB_STRATEGY.md
```

Suggested repository positioning, topics, and staged commits.

### Screenshot Checklist

```text
docs/SCREENSHOT_CHECKLIST.md
```

Recommended screenshots for professional GitHub/project evidence.

### Attached Specification

```text
docs/ATTACHED_SPECIFICATION.txt
```

The supplied project specification used as the basis for the implementation.

---

## Future Enhancements

Possible future improvements include:

- Role-based analyst authentication.
- More advanced correlation rules.
- Configurable scoring weights.
- Explainable risk-score breakdowns in the UI.
- Analyst case management.
- Exportable CSV/JSON investigation reports.
- More advanced trend analytics.
- Production-grade PostgreSQL support.
- Containerized deployment.
- Dashboard filtering by date, severity, IOC type, source, and status.
- Integration with approved and properly authorized CTI feeds in a controlled environment.

Any future integration with external intelligence sources should preserve the project's defensive and authorization boundaries.

---

## Quick Start

For a fast local setup on Windows:

```powershell
# 1. Create virtual environment
py -m venv .venv

# 2. Activate
.\.venv\Scripts\Activate.ps1

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Generate 2,000 synthetic records
python data\generate_threat_data.py

# 5. Start backend
python -m backend.app
```

Then open a second terminal:

```powershell
.\.venv\Scripts\Activate.ps1
cd frontend
python -m http.server 5500
```

Open:

```text
http://127.0.0.1:5500
```

---

## Author

**Ayush Kumar Dubey**

Student project focused on defensive cybersecurity, threat-intelligence analytics, security awareness, and portfolio development.

---

## Ethical Disclaimer

This project is provided strictly for **authorized defensive cybersecurity education, threat-intelligence analysis, security awareness, and academic/project demonstration**.

Do not use any part of the project to target systems, networks, accounts, or infrastructure without explicit authorization.

**Defensive analysis. Synthetic data. Authorized use only.**
