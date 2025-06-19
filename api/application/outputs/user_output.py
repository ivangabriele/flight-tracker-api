from uuid import UUID
from pydantic import BaseModel

from api.domain.entities import User


class UserOutput(BaseModel):
    id: UUID
    email: str

    @classmethod
    def from_user(cls, user: User) -> "UserOutput":
        return cls(id=user.id, email=user.email)
