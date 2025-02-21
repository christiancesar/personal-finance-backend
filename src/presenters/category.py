from uuid import UUID

from pydantic import BaseModel


class CategoryPresenter(BaseModel):
    id: UUID
    name: str
