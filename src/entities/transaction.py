from datetime import datetime
from enum import Enum
from uuid import UUID, uuid4

from entities.bank import Bank
from entities.category import Category
from entities.payment_type import PaymentType


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Transaction:
    def __init__(
        self,
        amount: float,
        paymentType: PaymentType,
        category: Category,
        bank: Bank,
        transaction_type: TransactionType,
        transaction_date: datetime,
        id: UUID = None,
    ):
        self.id = id if id else uuid4()
        self.amount = amount
        self.payment_type = TransactionType[paymentType]
        self.category = category
        self.bank = bank
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date
        self.created_at = datetime.now()
