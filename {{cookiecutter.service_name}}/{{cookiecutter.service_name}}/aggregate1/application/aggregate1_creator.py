from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1
from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1_repository import Aggregate1Repository


class Aggregate1Creator:
    def __init__(self, aggregate1_repository: Aggregate1Repository):
        self.aggregate1_repository = aggregate1_repository

    def invoke(self, aggregate1: Aggregate1):
        self.aggregate1_repository.store(aggregate1)
