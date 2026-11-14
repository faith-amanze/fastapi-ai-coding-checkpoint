from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_details_returns_status_service_and_version():
    response = client.get("/health-details")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "checkpoint-api",
        "version": "0.1.0",
    }


def test_health_details_returns_only_expected_keys():
    response = client.get("/health-details")
    assert response.status_code == 200
    assert set(response.json().keys()) == {"status", "service", "version"}
