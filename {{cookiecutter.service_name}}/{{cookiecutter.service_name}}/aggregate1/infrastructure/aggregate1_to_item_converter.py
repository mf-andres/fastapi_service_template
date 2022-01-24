from typing import List

from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1
from {{cookiecutter.service_name}}.entrypoint.items.aggregate1_item import Aggregate1Item


def convert_many(aggregate1s: List[Aggregate1]) -> List[Aggregate1Item]:
    return [convert(aggregate1) for aggregate1 in aggregate1s]


def convert(aggregate1: Aggregate1) -> Aggregate1Item:
    return Aggregate1Item(
        id_=aggregate1.id_,
        param1=aggregate1.param1,
    )