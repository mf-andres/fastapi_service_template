from pydantic import BaseSettings


class Settings(BaseSettings):
    aggregate1_repository_host: str
    aggregate1_repository_port: int
    aggregate1_repository_user: str
    aggregate1_repository_password: str
    aggregate1_repository_database_name: str
