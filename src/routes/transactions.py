from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from entities.transaction import Transaction, TransactionType
from presenters.transaction import TransactionPresenter
from repositories.in_memory.seeds.banks import banks
from repositories.in_memory.seeds.categories import categories
from repositories.in_memory.seeds.payment_types import payment_types
from repositories.in_memory.seeds.transactions import transactions

transactions_router = APIRouter(
    prefix="/transactions",
    tags=["transactions"],
)


class TransactionSchemaValidation(BaseModel):
    amount: float
    payment_type_id: UUID
    category_id: UUID
    bank_id: UUID
    transaction_type: TransactionType
    transaction_date: datetime


@transactions_router.post("/", response_model=TransactionPresenter)
def create_transaction(
    transaction: TransactionSchemaValidation,
):
    print(transaction)
    category_is_exist = any(
        category.id == transaction.category_id for category in categories
    )
    bank_is_exist = any(bank.id == transaction.bank_id for bank in banks)
    payment_type_is_exist = any(
        payment_type.id == transaction.payment_type_id for payment_type in payment_types
    )

    if not category_is_exist or not bank_is_exist or not payment_type_is_exist:
        raise HTTPException(
            status_code=400,
            detail={
                "message": "One or more fields are invalid",
                "fields": {
                    "category_is_exist": category_is_exist,
                    "bank_is_exist": bank_is_exist,
                    "payment_type_is_exist": payment_type_is_exist,
                },
            },
        )

    new_transaction = Transaction(
        amount=transaction.amount,
        paymentType=transaction.payment_type_id,
        category=transaction.category_id,
        bank=transaction.bank_id,
        transaction_type=transaction.transaction_type,
        transaction_date=transaction.transaction_date,
    )
    transactions.append(new_transaction)
    return new_transaction


@transactions_router.get("/", response_model=list[TransactionPresenter])
def get_transactions():
    return transactions
