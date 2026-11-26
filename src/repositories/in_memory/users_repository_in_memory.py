from entities.user import User
from repositories.users_repository_interface import (
    CreateUserRepositorySchemaValidation,
    UsersRepositoryInterface,
)


class UsersRepositoryInMemory(UsersRepositoryInterface):
    def __init__(self):
        self.users: list[User] = []

    def create_user(self, user: CreateUserRepositorySchemaValidation) -> User:
        new_user = User(
            email=user.email,
            password=user.password,
        )

        self.users.append(new_user)
        return new_user

    def get_user_by_email(self, email: str) -> User | None:
        for user in self.users:
            if user.email == email:
                return user
        return None


# Single shared instance. Every route must use this one; separate instances
# would each hold their own list, so a user created in one route would not
# exist for another (e.g. login).
users_repository_in_memory = UsersRepositoryInMemory()
