from datetime import datetime
from enum import Enum
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from .bank import BankPresenter
from .category import CategoryPresenter
from .payment_type import PaymentTypePresenter


class TransactionTypePresenter(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class InstallmentPresenter(BaseModel):
    id: UUID
    amount: float
    due_date: datetime
    paid_at: Optional[datetime]


class TransactionPresenter(BaseModel):
    id: UUID
    description: Optional[str]
    amount: float
    payment_type: CategoryPresenter
    category: PaymentTypePresenter
    bank: BankPresenter
    transaction_type: TransactionTypePresenter
    transaction_date: datetime
    transaction_date: datetime
    installment_count: int
    due_date_every: int
    installments: List[InstallmentPresenter]
