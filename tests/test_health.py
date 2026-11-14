from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_details_returns_service_info():
    response = client.get("/health-details")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "checkpoint-api",
        "version": "0.1.0",
    }


def test_health_details_exposes_only_expected_keys():
    body = client.get("/health-details").json()
    assert set(body) == {"status", "service", "version"}
