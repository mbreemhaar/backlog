from fastapi.testclient import TestClient


def test_health_check_returns_200(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_health_check_returns_ok_status(client: TestClient) -> None:
    response = client.get("/health")
    assert response.json()["status"] == "ok"


def test_readiness_check_returns_200(client: TestClient) -> None:
    response = client.get("/ready")
    assert response.status_code == 200


def test_readiness_check_returns_ok_status(client: TestClient) -> None:
    response = client.get("/ready")
    assert response.json()["status"] == "ok"
