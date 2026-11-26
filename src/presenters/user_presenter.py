from uuid import UUID

from pydantic import BaseModel, Field

from presenters.account_presenter import AccountPresenter
from presenters.profile_presenter import ProfilePresenter


class UserPresenter(BaseModel):
    id: UUID
    email: str
    password: str = Field(exclude=True)
    disabled: bool
    profile: ProfilePresenter | None
    account: AccountPresenter | None
