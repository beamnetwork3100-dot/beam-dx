from fastapi import FastAPI

app = FastAPI(
    title="Beam Dx API",
    description="Clinical Decision Support Platform for Laboratory Medicine",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "application": "Beam Dx",
        "status": "Running",
        "version": "0.1.0",
        "message": "Welcome to Beam Dx API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
