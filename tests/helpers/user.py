from uuid import UUID, uuid4
from api.infrastructure.models.user_model import UserModel
from tests.helpers.faker import faker
from sqlalchemy.orm import Session


def create_fake_user(
    session: Session, id: UUID = uuid4(), email: str = faker.email()
) -> UserModel:
    user = UserModel(id=id, email=email)
    session.add(user)
    session.flush()

    return user
