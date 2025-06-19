from typing import List
from uuid import UUID
from sqlalchemy.orm import Session

from api.domain.entities import User
from api.domain.ports.user_port import UserPort
from api.infrastructure.models import UserModel


class UserRepository(UserPort):
    session: Session

    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[User]:
        user_models = self.session.query(UserModel)
        users = [user_model.to_user() for user_model in user_models]

        return users

    def get_by_id(self, id: str) -> User | None:
        user_model = self.session.get(UserModel, UUID(id))
        if user_model is None:
            return None

        return user_model.to_user()
