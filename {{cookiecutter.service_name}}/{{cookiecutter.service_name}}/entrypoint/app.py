from dotenv import load_dotenv
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from {{cookiecutter.service_name}}.aggregate1.infrastructure.mongo_aggregate1_repository import MongoAggregate1Repository
from {{cookiecutter.service_name}}.entrypoint.routers import aggregate1_router, health_router
from {{cookiecutter.service_name}}.shared.infrastructure.settings import Settings

app = FastAPI(
    title="Authentication Service",
)


def inject_dependencies():
    load_dotenv(".dev.env")
    settings = Settings()
    app.aggregate1_repository = MongoAggregate1Repository(
        host=settings.aggregate1_repository_host,
        port=settings.aggregate1_repository_port,
        user=settings.aggregate1_repository_user,
        password=settings.aggregate1_repository_password,
        database_name=settings.aggregate1_repository_database_name,
    )


def include_routers():
    app.include_router(health_router.router, tags=["health"])
    app.include_router(aggregate1_router.router, tags=["aggregate1"])


def configure_cors():
    origins = ["http://localhost:4200"]
    app.add_middleware(
        CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )


inject_dependencies()
include_routers()
configure_cors()
