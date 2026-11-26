from uuid import UUID

from entities.entity import BaseEntity


class PaymentType(BaseEntity):
    def __init__(self, name: str, id: UUID | None = None):
        super().__init__(id)
        self.name = name
