from unittest.mock import Mock

from {{cookiecutter.service_name}}.aggregate1.application.aggregate1_creator import Aggregate1Creator
from tests.{{cookiecutter.service_name}}.aggregate1.utils import aggregate1_mother


def test_calls_birthday_repository():
    aggregate1_repository = Mock()
    aggregate1_repository.store = Mock()
    aggregate1_creator = Aggregate1Creator(aggregate1_repository)
    aggregate1 = aggregate1_mother.get_aggregate1()
    aggregate1_creator.invoke(aggregate1)
    aggregate1_repository.store.assert_called_once_with(aggregate1)