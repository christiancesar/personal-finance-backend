from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PaymentTypePresenter(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: Optional[datetime]
