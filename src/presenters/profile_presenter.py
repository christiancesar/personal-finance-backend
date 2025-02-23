from uuid import UUID

from pydantic import BaseModel


class ProfilePresenter(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    full_name: str
    email: str
    phone: str
