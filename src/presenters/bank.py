from uuid import UUID

from pydantic import BaseModel


class BankPresenter(BaseModel):
    id: UUID
    name: str
    fullName: str
    code: int
    ispb: str
