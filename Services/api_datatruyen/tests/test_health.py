from fastapi.testclient import TestClient
from server import app

client = TestClient(app)


def test_health_endpoint_returns_status():
    resp = client.get("/health")
    assert resp.status_code in (200, 503)
    data = resp.json()
    assert isinstance(data, dict)
    assert "status" in data