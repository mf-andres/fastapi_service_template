from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1
from {{cookiecutter.service_name}}.entrypoint.items.aggregate1_item import Aggregate1Item


def invoke(aggregate1_item: Aggregate1Item) -> Aggregate1:
    return Aggregate1(
        aggregate1_item.id_,
        aggregate1_item.param1,
    )