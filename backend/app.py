import os
from pathlib import Path
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from backend.services.database import init_db, seed_database
from backend.routes.api import api

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "local-development-secret")
    app.config["DATABASE_PATH"] = os.getenv("DATABASE_PATH", str(BASE_DIR / "instance" / "dashboard.db"))
    CORS(app)
    Path(app.config["DATABASE_PATH"]).parent.mkdir(parents=True, exist_ok=True)
    init_db(app.config["DATABASE_PATH"])
    seed_database(app.config["DATABASE_PATH"])
    app.register_blueprint(api, url_prefix="/api")
    @app.get("/api/health")
    def health():
        return {"status": "ok", "mode": "synthetic-demo"}
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
