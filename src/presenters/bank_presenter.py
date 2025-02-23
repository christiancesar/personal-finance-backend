from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class BankPresenter(BaseModel):
    id: UUID
    name: str
    fullName: str
    code: int
    ispb: str
    created_at: datetime
    updated_at: Optional[datetime]
