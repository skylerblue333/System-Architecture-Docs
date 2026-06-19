from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_register_service():
    r = client.post("/api/v1/services", json={
        "name": "auth-service",
        "language": "Go",
        "description": "JWT authentication",
        "endpoints": ["/login", "/refresh"]
    })
    assert r.status_code == 200
    assert r.json()["status"] == "registered"

def test_list_services():
    r = client.get("/api/v1/services")
    assert r.status_code == 200
    assert "services" in r.json()

