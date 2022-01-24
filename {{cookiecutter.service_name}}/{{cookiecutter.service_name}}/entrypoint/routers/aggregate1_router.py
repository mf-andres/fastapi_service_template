from fastapi import APIRouter
from fastapi import Request

from {{cookiecutter.service_name}}.aggregate1.application.aggregate1_creator import Aggregate1Creator
from {{cookiecutter.service_name}}.aggregate1.infrastructure import item_to_aggregate1_converter
from {{cookiecutter.service_name}}.entrypoint.items.aggregate1_item import Aggregate1Item

router = APIRouter()


@router.post(
    "/aggregate1",
    status_code=201,
    response_model=None,
)
def post(request: Request, aggregate1: Aggregate1Item):
    aggregate1 = item_to_aggregate1_converter.invoke(aggregate1)
    aggregate1_repository = request.app.aggregate1_repository
    aggregate1_creator = Aggregate1Creator(aggregate1_repository)
    aggregate1_creator.invoke(aggregate1)

