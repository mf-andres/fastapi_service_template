from tests.{{cookiecutter.service_name}}.aggregate1.utils import aggregate1_mother


def test_stores_one_aggregate1(mongo_aggregate1_repository_setup_and_teardown):
    mongo_aggregate1_repository = mongo_aggregate1_repository_setup_and_teardown
    aggregate1 = aggregate1_mother.get_aggregate1()
    mongo_aggregate1_repository.store(aggregate1)
    aggregates = mongo_aggregate1_repository.retrieve(aggregate1.id_)
    assert len(aggregates) == 1


def test_updates_one_aggregate1(mongo_aggregate1_repository_setup_and_teardown):
    mongo_aggregate1_repository = mongo_aggregate1_repository_setup_and_teardown
    aggregate1 = aggregate1_mother.get_aggregate1()
    mongo_aggregate1_repository.store(aggregate1)
    aggregate1.param1 = "param1_2"
    mongo_aggregate1_repository.update(aggregate1)
    aggregates = mongo_aggregate1_repository.retrieve(aggregate1.id_)
    assert aggregates[0].param1 == aggregate1.param1


def test_removes_one_aggregate1(mongo_aggregate1_repository_setup_and_teardown):
    mongo_aggregate1_repository = mongo_aggregate1_repository_setup_and_teardown
    aggregate1 = aggregate1_mother.get_aggregate1()
    mongo_aggregate1_repository.store(aggregate1)
    mongo_aggregate1_repository.remove(aggregate1.id_)
    aggregates = mongo_aggregate1_repository.retrieve(aggregate1.id_)
    assert len(aggregates) == 0
