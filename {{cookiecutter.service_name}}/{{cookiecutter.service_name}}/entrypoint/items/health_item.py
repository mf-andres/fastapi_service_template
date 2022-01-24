from pydantic import BaseModel


class HealthItem(BaseModel):
    aggregate1_repository_reachable: bool
