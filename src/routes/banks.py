from fastapi import APIRouter

from presenters.bank_presenter import BankPresenter
from repositories.in_memory.seeds.banks_seed import banks

banks_router = APIRouter(
    prefix="/banks",
    tags=["banks"],
)


@banks_router.get("/", response_model=list[BankPresenter])
def get_banks():
    return banks
