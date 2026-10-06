# VS Code / Windows Run Guide

## 1. Open the project
Extract the ZIP and open the folder `Cybersecurity-Awareness-Threat-Intelligence-Dashboard` in VS Code.

## 2. Open PowerShell terminal
In VS Code: Terminal → New Terminal.

## 3. Create virtual environment
```powershell
py -m venv .venv
```

## 4. Activate it
```powershell
.\.venv\Scripts\Activate.ps1
```
If PowerShell blocks activation, use:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 5. Install dependencies
```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 6. Generate/re-generate the 2,000-record synthetic dataset
```powershell
python data\generate_threat_data.py
```

## 7. Initialize the local SQLite database
The Flask app creates and seeds the database automatically on startup. To force a clean database:
```powershell
Remove-Item .\instance\dashboard.db -ErrorAction SilentlyContinue
```

## 8. Start backend
```powershell
python -m backend.app
```
Keep this terminal running. Backend:
`http://127.0.0.1:8000`

Health check:
`http://127.0.0.1:8000/api/health`

## 9. Start frontend
Open a **second** VS Code terminal:
```powershell
cd frontend
python -m http.server 5500
```
Frontend:
`http://127.0.0.1:5500`

## 10. Open dashboard
Browser:
`http://127.0.0.1:5500`

## 11. Test IOC search
Use:
`198.51.100.25`
or
`example.com`

The application only searches its local SQLite database. It does not contact the indicator.

## 12. Threat details
Open `threat-details.html` and enter a threat ID such as:
`THR-2026-0001`

## 13. Awareness Center
Open:
`http://127.0.0.1:5500/awareness.html`

## 14. Quiz
Open:
`http://127.0.0.1:5500/quiz.html`

## 15. Run tests
From project root:
```powershell
pytest -q
```

## 16. Useful API commands
```powershell
Invoke-RestMethod http://127.0.0.1:8000/api/health
Invoke-RestMethod http://127.0.0.1:8000/api/dashboard/stats
Invoke-RestMethod "http://127.0.0.1:8000/api/indicators/search?q=198.51.100.25"
Invoke-RestMethod http://127.0.0.1:8000/api/vulnerabilities
Invoke-RestMethod http://127.0.0.1:8000/api/executive-summary
```

## 17. Stop the project
Press `Ctrl+C` in both terminals.

## Common issues
- `ModuleNotFoundError`: confirm `.venv` is active and run `pip install -r requirements.txt`.
- Port 8000 busy: stop the old Python process or change the port in `backend/app.py`.
- Frontend CORS error: make sure backend is running on `127.0.0.1:8000`.
- Empty database: delete `instance/dashboard.db` and restart backend.
