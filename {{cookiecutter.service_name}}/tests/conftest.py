import pytest

from {{cookiecutter.service_name}}.aggregate1.infrastructure.mongo_aggregate1_repository import MongoAggregate1Repository
from {{cookiecutter.service_name}}.shared.infrastructure.settings import Settings

settings = Settings()


@pytest.fixture
def mongo_aggregate1_repository_setup_and_teardown() -> MongoAggregate1Repository:
    aggregate1_repository = MongoAggregate1Repository(
        host=settings.aggregate1_repository_host,
        port=settings.aggregate1_repository_port,
        user=settings.aggregate1_repository_user,
        password=settings.aggregate1_repository_password,
        database_name=settings.aggregate1_repository_database_name,
    )
    aggregate1_repository.empty()
    yield aggregate1_repository
    aggregate1_repository.empty()
