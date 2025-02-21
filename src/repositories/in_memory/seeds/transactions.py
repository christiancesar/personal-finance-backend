from datetime import datetime

from entities.transaction import Transaction

from .banks import banks
from .categories import categories
from .payment_types import payment_types

transactions = [
    Transaction(
        amount=100.3,
        description="Test transaction",
        installment_count=2,
        payment_type=payment_types[0],
        category=categories[0],
        bank=banks[0],
        transaction_type="expense",
        transaction_date=datetime.now(),
    ),
    Transaction(
        amount=200,
        description="Test transaction",
        installment_count=2,
        payment_type=payment_types[0],
        category=categories[0],
        bank=banks[0],
        transaction_type="expense",
        transaction_date=datetime.now(),
    ),
    Transaction(
        amount=180,
        description="Test transaction",
        installment_count=2,
        payment_type=payment_types[0],
        category=categories[0],
        bank=banks[0],
        transaction_type="expense",
        transaction_date=datetime.now(),
    ),
    Transaction(
        amount=150,
        description="Test transaction",
        installment_count=2,
        payment_type=payment_types[0],
        category=categories[0],
        bank=banks[0],
        transaction_type="expense",
        transaction_date=datetime.now(),
    ),
    Transaction(
        amount=120,
        description="Test transaction",
        installment_count=2,
        payment_type=payment_types[0],
        category=categories[0],
        bank=banks[0],
        transaction_type="expense",
        transaction_date=datetime.now(),
    ),
]
