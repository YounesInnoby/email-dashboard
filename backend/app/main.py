# main.py
import uvicorn
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from email_service import get_emails

app = FastAPI()

# Pfad zu ./build neben main.py
FRONTEND_DIR = Path(__file__).parent / "build"

# Statische Dateien unter /app servieren
app.mount("/app", StaticFiles(directory=FRONTEND_DIR, html=True), name="app")

# SPA-Fallback: alle unbekannten Pfade unter /app -> index.html
@app.get("/app/{path:path}")
def spa_catch_all(path: str):
  index = FRONTEND_DIR / "index.html"
  return FileResponse(index)

# CORS (falls du im Dev getrennte Ports nutzt)
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/emails")
def fetch_emails():
  return JSONResponse(content=get_emails())

VALID_USER = "admin"
VALID_PASS = "admin"

class LoginIn(BaseModel):
  username: str
  password: str

@app.post("/api/login")
def login(body: LoginIn):
  if body.username == VALID_USER and body.password == VALID_PASS:
    return {"token": "dummy-token-123", "role": "user"}
  raise HTTPException(status_code=401, detail="Invalid credentials")

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8001)
