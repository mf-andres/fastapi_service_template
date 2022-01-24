from starlette.testclient import TestClient

from {{cookiecutter.service_name}}.entrypoint.app import app
from tests.{{cookiecutter.service_name}}.aggregate1.utils import aggregate1_mother


def test_adds_aggregate1_to_repository(mongo_aggregate1_repository_setup_and_teardown):
    client = TestClient(app)
    request_body = aggregate1_mother.get_aggregate_1_item().dict()
    response = client.post("/aggregate1", json=request_body)
    saved_aggregates = app.aggregate1_repository.retrieve(request_body["id_"])
    assert response.status_code == 201 and len(saved_aggregates) == 1
