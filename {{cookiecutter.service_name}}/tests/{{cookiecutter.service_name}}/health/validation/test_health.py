from starlette.testclient import TestClient

from {{cookiecutter.service_name}}.entrypoint.app import app


def test_returns_correct_status():
    client = TestClient(app)
    response = client.get("/health")
    response_body = response.json()
    all_connections_are_healthy = (
        response_body["aggregate1_repository_reachable"]
    )
    assert response.status_code == 200 and all_connections_are_healthy
