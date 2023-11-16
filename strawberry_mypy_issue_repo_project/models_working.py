import strawberry
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'Jane Doe'

@strawberry.experimental.pydantic.type(model=User)
class UserType:
    id: strawberry.auto
    name: strawberry.auto
