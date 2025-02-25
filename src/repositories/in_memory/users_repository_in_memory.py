from typing import List

from entities.roles import Roles
from entities.user import User
from repositories.users_repository_interface import (
    CreateUserRepositorySchemaValidation,
    UsersRepositoryInterface,
)


class UsersRepositoryInMemory(UsersRepositoryInterface):
    def __init__(self):
        self.users: List[User] = []

    def create_user(self, user: CreateUserRepositorySchemaValidation) -> User:
        new_user = User(
            email=user.email,
            password=user.password,
            roles=[Roles.ADMIN],
        )

        self.users.append(new_user)
        return new_user

    def get_user_by_email(self, email: str) -> User | None:
        for user in self.users:
            if user.email == email:
                return user
        return None
