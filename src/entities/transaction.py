from datetime import datetime, timedelta
from enum import Enum
from typing import List, Optional
from uuid import UUID

from entities.bank import Bank
from entities.category import Category
from entities.entity import BaseEntity
from entities.payment_type import PaymentType


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Installment(BaseEntity):
    def __init__(
        self,
        amount: float,
        due_date: datetime,
        paid_at: Optional[datetime] = None,
        id: Optional[UUID] = None,
    ):
        super().__init__(id)
        self.amount = amount
        self.due_date = due_date
        self.paid_at = paid_at

    def is_paid(self) -> bool:
        return self.paid_at is not None


"""Data de vencimento para pagamento das parcelas, quando o pagamento for no cartão de crédito"""
DEFAULT_DUE_DATE_EVERY = 30


class Transaction(BaseEntity):
    def __init__(
        self,
        amount: float,
        payment_type: PaymentType,
        category: Category,
        bank: Bank,
        transaction_type: TransactionType,
        transaction_date: datetime,
        description: Optional[str] = None,
        installment_count: int = 1,
        due_date_every: int = DEFAULT_DUE_DATE_EVERY,
        installments: List[Installment] = None,
        id: Optional[UUID] = None,
    ):
        super().__init__(id)
        self.amount = amount
        self.installment_count = installment_count
        self.description = description
        self.payment_type = payment_type
        self.category = category
        self.bank = bank
        self.transaction_type = transaction_type
        self.transaction_date = transaction_date
        self.due_date_every = due_date_every
        if installments is not None:
            self.installments = installments
        else:
            self.installments = []
            self.__create_installments()

    def __validate_installment_count(self, installment_count: int):
        if int(installment_count) < 1 or not isinstance(installment_count, int):
            return 1

    def __create_installments(self):
        if self.installment_count >= 1:
            previous_due_date = self.transaction_date
            for i in range(self.installment_count):
                due_date = previous_due_date + timedelta(days=self.due_date_every)
                self.installments.append(
                    Installment(
                        amount=self.amount / self.installment_count,
                        due_date=due_date,
                    )
                )
                previous_due_date = due_date
