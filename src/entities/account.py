from typing import Optional
from uuid import UUID

from .bank import Bank
from .entity import EntityBase


class Account(EntityBase):
    def __init__(self, name: str, id: Optional[UUID] = None):
        super().__init__(id)
        self.name = name
        self.balance = 0.0
        self.incomes = 0.0
        self.expenses = 0.0
        self.bank = Bank
        self.accounts
