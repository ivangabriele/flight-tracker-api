from uuid import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as SQL_UUID


from api.adapters import database as db
from api.domain.entities import User


class UserModel(db.Model):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(SQL_UUID(as_uuid=True), primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)

    def __init__(self, id: UUID, email: str):
        self.id = id
        self.email = email

    def to_user(self) -> User:
        return User(id=self.id, email=self.email)
