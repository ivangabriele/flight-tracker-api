from abc import ABC, abstractmethod
from typing import List, Optional

from api.domain.entities import User


class UserPort(ABC):
    @abstractmethod
    def get_all(self) -> List[User]:
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[User]:
        raise NotImplementedError()
