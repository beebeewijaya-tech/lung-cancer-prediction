from pydantic import BaseModel


class Person(BaseModel):
    age: int
    alcohol_consuming: bool
    wheezing: bool
    allergy: bool
    chest_pain: bool
