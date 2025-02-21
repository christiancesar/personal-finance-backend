from fastapi import APIRouter

from presenters.payment_type import PaymentTypePresenter
from repositories.in_memory.seeds.payment_types import payment_types

payment_types_router = APIRouter(
    prefix="/payment-types",
    tags=["payment-types"],
)


@payment_types_router.get("/", response_model=list[PaymentTypePresenter])
def get_payment_types():
    return payment_types
