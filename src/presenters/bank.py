from uuid import UUID

from pydantic import BaseModel


class BankPresenter(BaseModel):
    ispb: str
    name: str
    code: int
    fullName: str
    id: UUID
