from typing import Optional
from uuid import UUID

from entities.entity import BaseEntity


class Bank(BaseEntity):
    def __init__(
        self, ispb: str, name: str, code: int, fullName: str, id: Optional[UUID] = None
    ):
        super().__init__(id)
        self.name = name
        self.ispb = ispb
        self.code = code
        self.fullName = fullName
