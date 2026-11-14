from fastapi import FastAPI

app = FastAPI()

SERVICE_NAME = "checkpoint-api"
SERVICE_VERSION = "0.1.0"


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/health-details")
def health_details() -> dict[str, str]:
    return {
        "status": "ok",
        "service": SERVICE_NAME,
        "version": SERVICE_VERSION,
    }
