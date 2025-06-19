from typing import List, Optional

from api.domain.ports.user_port import UserPort
from api.domain.entities import User


def get_users(user_repository: UserPort) -> List[User]:
    return user_repository.get_all()


def get_user_by_id(user_repository: UserPort, id: str) -> Optional[User]:
    return user_repository.get_by_id(id)
