from uuid import UUID

from pydantic import BaseModel


class PaymentTypePresenter(BaseModel):
    id: UUID
    name: str
