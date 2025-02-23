from typing import List
from uuid import UUID

from pydantic import BaseModel

from presenters.bank_presenter import BankPresenter
from presenters.transaction_presenter import TransactionPresenter


class AccountPresenter(BaseModel):
    id: UUID
    name: str
    bank: BankPresenter
    balance: float
    incomes: float
    expenses: float
    transactions: List[TransactionPresenter] | None
