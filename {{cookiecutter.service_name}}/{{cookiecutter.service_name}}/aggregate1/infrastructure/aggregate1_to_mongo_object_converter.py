from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1


def convert(aggregate1: Aggregate1) -> dict:
    return {
        "id_": aggregate1.id_,
        "param1": aggregate1.param1,
    }
