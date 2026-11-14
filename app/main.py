from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


SERVICE_NAME = "checkpoint-api"
SERVICE_VERSION = "0.1.0"


@app.get("/health-details")
def health_details() -> dict:
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
    }
