from uuid import UUID

from .account import Account
from .entity import BaseEntity
from .profile import Profile


class User(BaseEntity):
    def __init__(
        self,
        email: str,
        password: str,
        disabled: bool = False,
        profile: Profile | None = None,
        account: Account | None = None,
        id: UUID | None = None,
    ):
        super().__init__(id)
        self.email = email
        self.password = password
        self.disabled = disabled
        self.profile = profile
        self.account = account
