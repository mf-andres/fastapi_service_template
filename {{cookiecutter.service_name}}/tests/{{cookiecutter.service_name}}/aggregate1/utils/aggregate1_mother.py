from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1
from {{cookiecutter.service_name}}.entrypoint.items.aggregate1_item import Aggregate1Item


def get_aggregate1():
    id_ = "id_"
    param1 = "param1"
    aggregate1 = Aggregate1(id_, param1)
    return aggregate1


def get_aggregate1_item():
    id_ = "id_"
    param1 = "param1"
    aggregate1_item = Aggregate1Item(id_=id_, param1=param1)
    return aggregate1_item
