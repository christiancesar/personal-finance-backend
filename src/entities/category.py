from typing import Optional
from uuid import UUID

from entities.entity import BaseEntity


class Category(BaseEntity):
    def __init__(self, name: str, id: Optional[UUID] = None):
        super().__init__(id)
        self.name = name
