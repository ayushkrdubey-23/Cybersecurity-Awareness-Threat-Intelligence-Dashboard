# Project Report — Cybersecurity Awareness & Threat Intelligence Dashboard

## Abstract
This project presents a defensive cybersecurity dashboard that combines synthetic cyber threat intelligence with security-awareness education. The platform normalizes and validates indicators, enriches them using local data, calculates risk and confidence, correlates related observations, manages alerts, presents vulnerability awareness, and maps selected synthetic observations to MITRE ATT&CK concepts. A separate awareness center provides learning modules and a 30-question quiz with educational scoring and recommendations.

## Introduction
Modern security teams combine technical intelligence with human awareness. An indicator by itself is not proof of compromise; context, confidence and analyst validation are essential. This project demonstrates that principle using safe local data.

## Problem Statement
Students need a realistic way to demonstrate SOC, threat-intelligence and awareness concepts without interacting with malicious infrastructure.

## Objectives
- Build a unified defensive dashboard.
- Generate at least 2,000 synthetic records.
- Validate IOC syntax without claiming maliciousness.
- Score risk and confidence separately.
- Demonstrate correlation, alerting and vulnerability prioritization.
- Teach security awareness.
- Provide reproducible testing and documentation.

## Cybersecurity Awareness
Awareness helps users recognize phishing, unsafe attachments, password reuse, social engineering, insecure Wi-Fi, privacy risks and incident-reporting needs.

## Cyber Threat Intelligence
CTI supports defensive decisions by collecting, normalizing, contextualizing and communicating threat information.

## Threat Intelligence Types
Strategic intelligence supports leadership decisions; tactical intelligence describes adversary behavior and defensive patterns; operational intelligence supports campaigns and investigations; technical intelligence focuses on artifacts such as IOCs. This project emphasizes technical, tactical and awareness-oriented intelligence.

## IOC and IOA Concepts
An IOC is an observable artifact that may be associated with malicious activity. An IOA describes behavior indicating possible malicious activity. Neither should be treated without context as automatic proof of compromise.

## Threat Intelligence Lifecycle
Collection → normalization → validation → extraction → classification → scoring → mapping → storage → correlation → analyst review → awareness/remediation.

## Proposed System
The system uses Flask, SQLite, Pandas, HTML/CSS/JavaScript and local JSON/CSV datasets.

## Architecture
Synthetic data enters a local ingestion/database layer, passes through validation, enrichment, risk/confidence and correlation logic, and is presented through a SOC dashboard. Awareness content runs in parallel through modules, quiz scoring and recommendations.

## Synthetic Dataset
The generator creates 2,000 safe records using documentation IP ranges, example domains, fictional URLs, synthetic hashes and synthetic CVE-style identifiers. Records are explicitly labeled SYNTHETIC / DEMO ONLY.

## IOC Validation
Validation asks whether a value has the expected syntax. It does not ask whether the value is malicious.

## Threat Enrichment
Enrichment adds local category, dates, confidence, severity, risk, alerts, related indicators and conservative ATT&CK context.

## Risk Scoring
The demo model weights severity 30%, confidence 25%, recency 15%, observation frequency 10%, source reliability 10% and context/correlation 10%. The result is 0–100.

## Confidence Scoring
Confidence measures evidence quality separately from concern level.

## Source Reliability
Synthetic sources use A/B/C/D reliability levels. Source reliability and item confidence are related but distinct.

## Threat Correlation
Records can be grouped using shared campaign, category and observation-window evidence. Correlation does not prove attribution.

## MITRE ATT&CK
Selected mappings use high-level current terminology only when the synthetic category provides enough context. Mapping is educational, not attribution.

## Vulnerability Awareness
Synthetic vulnerability records demonstrate why CVSS should be combined with asset criticality, exposure, exploitation evidence and business context.

## Alert Management
High-risk/high-confidence synthetic records can create demo alerts. Alert correlation reduces duplicate analyst workload conceptually.

## SOC Workflow
Feed → IOC → validation → enrichment → risk/confidence → alert → queue → triage → correlation → investigation → monitor/escalate/resolve/false-positive → documentation.

## Awareness Center
Fifteen modules cover phishing, passwords, MFA, social engineering, browsing, Wi-Fi, updates, ransomware, removable media, privacy, mobile, remote work, cloud accounts, reporting and AI-enabled scams.

## Quiz System
The quiz contains 30 questions. Scores are converted to educational categories: Needs Improvement, Basic Awareness, Good Awareness and Strong Awareness.

## Executive Dashboard
Management-facing information includes threat counts, categories, vulnerability groups, awareness weaknesses and recommended defensive priorities.

## Testing
Core services have automated tests. A 35-item test plan is included for broader validation.

## Security
The application does not contact indicators. Production deployment would require authentication, RBAC, HTTPS, rate limiting, audit logging and stronger operational controls.

## Results
The resulting prototype provides a complete local workflow from synthetic data generation to analyst-facing dashboard and awareness education.

## Limitations
The dataset is synthetic. The demo has no live feeds, no external enrichment and no production identity system. ATT&CK mappings are conservative educational mappings.

## Future Scope
Future defensive enhancements could include controlled public-feed ingestion, richer RBAC, PostgreSQL, React/FastAPI, audit logs, scheduled ingestion, SIEM connectors and production-grade observability.

## Conclusion
The project demonstrates how threat intelligence, analyst context and human awareness can be combined in a safe educational SOC-style application.

## Ethical Disclaimer
This project is designed exclusively for defensive cybersecurity education, threat-intelligence analysis, and security awareness. It does not execute, deploy, or interact with malicious payloads or unauthorized systems.
