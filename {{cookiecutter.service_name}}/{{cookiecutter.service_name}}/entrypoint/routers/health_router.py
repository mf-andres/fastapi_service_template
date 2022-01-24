from fastapi import APIRouter, Request

from {{cookiecutter.service_name}}.entrypoint.items.health_item import HealthItem

router = APIRouter()


@router.get(
    "/health",
    description="Checks service health",
    status_code=200,
    response_model=HealthItem,
)
def get_health(request: Request):
    aggregate1_repository_reachable = request.app.aggregate1_repository.is_reachable()
    health_item = HealthItem(
        aggregate1_repository_reachable=aggregate1_repository_reachable,
    )
    return health_item
