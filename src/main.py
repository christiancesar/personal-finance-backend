from datetime import datetime
from uuid import UUID

from fastapi import FastAPI
from pydantic import BaseModel

from entities.category import Category
from entities.transaction import Transaction, TransactionType
from repositories.in_memory.seeds.banks import banks
from repositories.in_memory.seeds.categories import categories
from repositories.in_memory.seeds.payment_types import payment_types
from repositories.in_memory.seeds.transactions import transactions

app = FastAPI()


class CategorySchemaValidation(BaseModel):
    name: str


@app.post("/api/v1/categories")
def create_category(category: CategorySchemaValidation):
    new_category = Category(name=category.name)
    categories.append(new_category)
    return new_category


@app.get("/api/v1/categories")
def get_categories():
    return categories


@app.get("/api/v1/banks")
def get_banks():
    return banks


@app.get("/api/v1/payment-types")
def get_payment_types():
    return payment_types


class TransactionSchemaValidation(BaseModel):
    amount: float
    payment_type_id: UUID
    category_id: UUID
    bank_id: UUID
    transaction_type: TransactionType
    transaction_date: datetime


@app.post("/api/v1/transactions")
def create_transaction(transaction: TransactionSchemaValidation):
    print(transaction)
    category_is_exist = transaction.category_id in categories
    bank_is_exist = transaction.bank_id in banks
    payment_type_is_exist = transaction.payment_type_id in payment_types

    if not category_is_exist or not bank_is_exist or not payment_type_is_exist:
        return {
            "message": "One or more fields are invalid",
            "fields": {
                "category_is_exist": category_is_exist,
                "bank_is_exist": bank_is_exist,
                "payment_type_is_exist": payment_type_is_exist,
            },
        }
    else:
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


@app.get("/api/v1/transactions")
def get_transactions():
    return transactions
