from typing import List

from entities.roles import Roles
from entities.user import User

users: List[User] = [
    User(
        email="example@mail.com",
        password="12345678",
        roles=[Roles.OWNER, Roles.ADMIN],
    ),
    User(
        email="example@mail.com",
        password="12345678",
        roles=[Roles.ASSISTANT],
    ),
]
