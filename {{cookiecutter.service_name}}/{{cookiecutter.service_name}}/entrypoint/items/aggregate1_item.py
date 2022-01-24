from pydantic import BaseModel


class Aggregate1Item(BaseModel):
    id_: str
    param1: str
