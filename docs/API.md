# API Reference

All endpoints are local and operate on synthetic/demo data.

| Method | Endpoint | Purpose | Validation | Auth |
|---|---|---|---|---|
| GET | /api/threats | List/filter threats | Query filters | Demo-local |
| GET | /api/threats/{id} | Threat detail | Threat ID | Demo-local |
| GET | /api/indicators/search?q= | Local IOC lookup | IOC format | Demo-local |
| GET | /api/dashboard/stats | Executive counters | None | Demo-local |
| GET | /api/dashboard/trends | Chart datasets | None | Demo-local |
| GET | /api/alerts | Alert queue | None | Demo-local |
| PUT | /api/alerts/{id}/status | Update alert status | Allow-list status | Demo-local |
| POST | /api/threats/{id}/notes | Add analyst note | Non-empty note | Demo-local |
| GET | /api/vulnerabilities | Vulnerability list | None | Demo-local |
| GET | /api/awareness/modules | Learning content | None | Demo-local |
| GET | /api/quiz | Quiz questions | None | Demo-local |
| POST | /api/quiz/submit | Score quiz | JSON answers | Demo-local |

**Production note:** real deployments should add authentication, RBAC, rate limiting, audit logging, HTTPS, CSRF protection where relevant, secret management and stronger input/output controls.
