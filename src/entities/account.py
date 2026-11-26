from uuid import UUID

from .bank import Bank
from .entity import BaseEntity
from .transaction import Transaction


class Account(BaseEntity):
    def __init__(
        self,
        name: str,
        bank: Bank,
        balance: float = 0.0,
        incomes: float = 0.0,
        expenses: float = 0.0,
        transactions: list[Transaction] | None = [],
        id: UUID | None = None,
    ):
        super().__init__(id)
        self.name = name
        self.balance = balance
        self.incomes = incomes
        self.expenses = expenses
        self.bank = bank
        self.transactions = transactions
