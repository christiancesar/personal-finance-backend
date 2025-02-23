from typing import List
from uuid import UUID

from .account import Account
from .entity import BaseEntity
from .profile import Profile
from .roles import Roles


class User(BaseEntity):
    def __init__(
        self,
        email: str,
        password: str,
        roles: List[Roles],
        disabled: bool = False,
        profile: Profile | None = None,
        account: Account | None = None,
        id: UUID | None = None,
    ):
        super().__init__(id)
        self.email = email
        self.password = password
        self.disabled = disabled
        self.roles = roles
        self.profile = profile
        self.account = account
