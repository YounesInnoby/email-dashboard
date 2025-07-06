import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from email_service import get_emails
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/app", StaticFiles(directory="build", html=True), name="static")

# CORS für Frontend-Zugriff aktivieren
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
56701