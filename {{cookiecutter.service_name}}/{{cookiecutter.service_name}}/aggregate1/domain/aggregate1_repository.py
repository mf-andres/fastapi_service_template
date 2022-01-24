import abc

from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1


class Aggregate1Repository(abc.ABC):
    @abc.abstractmethod
    def store(self, aggregate1: Aggregate1):
        pass
