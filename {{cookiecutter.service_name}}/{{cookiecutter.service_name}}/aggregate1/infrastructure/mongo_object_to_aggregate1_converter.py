from datetime import date, datetime
from typing import List

from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1


def convert_many(aggregate1s_as_dict: List[dict]) -> List[Aggregate1]:
    return [convert(aggregate1_as_dict) for aggregate1_as_dict in aggregate1s_as_dict]


def convert(aggregate1_as_dict: dict) -> Aggregate1:
    return Aggregate1(
        aggregate1_as_dict["id_"],
        aggregate1_as_dict["param1"],
    )
