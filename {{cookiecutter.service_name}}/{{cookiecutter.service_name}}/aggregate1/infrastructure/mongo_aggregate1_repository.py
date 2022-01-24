
from typing import List

from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1 import Aggregate1
from {{cookiecutter.service_name}}.aggregate1.domain.aggregate1_repository import Aggregate1Repository
from {{cookiecutter.service_name}}.aggregate1.infrastructure import aggregate1_to_mongo_object_converter, \
    mongo_object_to_aggregate1_converter
from {{cookiecutter.service_name}}.shared.infrastructure.mongo_repository import MongoRepository


class MongoAggregate1Repository(MongoRepository, Aggregate1Repository):
    def __init__(
            self,
            host=str,
            port=int,
            user=str,
            password=str,
            database_name=str,
    ):
        collection_name = "aggregates"
        super().__init__(
            host,
            port,
            user,
            password,
            database_name,
            collection_name
        )

    def store(self, aggregate1: Aggregate1):
        aggregate1_as_dict = aggregate1_to_mongo_object_converter.convert(aggregate1)
        self.collection.insert_one(aggregate1_as_dict)

    def update(self, aggregate1: Aggregate1):
        query = {"id_": aggregate1.id_}
        aggregate1_as_dict = aggregate1_to_mongo_object_converter.convert(aggregate1)
        update = {
            "$set": {
                "param1": aggregate1_as_dict["param1"],
            }
        }
        self.collection.update_one(query, update)

    def remove(self, aggregate1_id: str):
        query = {"id_": aggregate1_id}
        self.collection.delete_one(query)

    def retrieve(self, id_: str) -> List[Aggregate1]:
        query = {"id_": id_}
        cursor = self.collection.find(query, {"id": False})
        aggregates_as_dict = list(cursor)
        aggregates = mongo_object_to_aggregate1_converter.convert_many(aggregates_as_dict)
        return aggregates

    def empty(self):
        self.collection.delete_many({})
