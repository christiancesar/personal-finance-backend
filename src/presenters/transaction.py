from datetime import datetime
from enum import Enum
from uuid import UUID

from pydantic import BaseModel

from .bank import BankPresenter
from .category import CategoryPresenter
from .payment_type import PaymentTypePresenter


class TransactionTypePresenter(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class TransactionPresenter(BaseModel):
    amount: float
    paymentType: CategoryPresenter
    category: PaymentTypePresenter
    bank: BankPresenter
    transaction_type: TransactionTypePresenter
    transaction_date: datetime
    id: UUID
