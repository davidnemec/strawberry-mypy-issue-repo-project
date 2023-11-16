import strawberry

from strawberry_mypy_issue_repo_dependency.models import User


@strawberry.experimental.pydantic.type(model=User)
class UserType:
    id: strawberry.auto
    name: strawberry.auto
