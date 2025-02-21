from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from entities.bank import Bank
from entities.category import Category
from entities.payment_type import PaymentType
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
    installment_count: int
    due_date_every: int


@transactions_router.post("/", response_model=TransactionPresenter)
def create_transaction(
    transaction_request_body: TransactionSchemaValidation,
):
    category_is_exist: Category = None
    bank_is_exist: Bank = None
    payment_type_is_exist: PaymentType = None
    for category in categories:
        if category.id == transaction_request_body.category_id:
            category_is_exist = category

    for bank in banks:
        if bank.id == transaction_request_body.bank_id:
            bank_is_exist = bank

    for payment_type in payment_types:
        if payment_type.id == transaction_request_body.payment_type_id:
            payment_type_is_exist = payment_type

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
        amount=transaction_request_body.amount,
        payment_type=payment_type_is_exist,
        category=category_is_exist,
        bank=bank_is_exist,
        transaction_type=transaction_request_body.transaction_type,
        transaction_date=transaction_request_body.transaction_date,
        installment_count=transaction_request_body.installment_count,
        due_date_every=transaction_request_body.installment_count,
    )

    transactions.append(new_transaction)

    return new_transaction


@transactions_router.get("/", response_model=list[TransactionPresenter])
def get_transactions():
    return transactions
