from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class PaymentTypePresenter(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime | None
