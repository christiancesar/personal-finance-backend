from pydantic import BaseModel, EmailStr, Field

from entities.user import User
from providers.password_hashed.interfaces.password_hashed_interface_provider import (
    PasswordHasherInterfaceProvider,
)
from repositories.users_repository_interface import (
    CreateUserRepositorySchemaValidation,
    UsersRepositoryInterface,
)


class CreateUserSchemaValidation(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class CreateUserService:
    def __init__(
        self,
        repository: UsersRepositoryInterface,
        password_hasher: PasswordHasherInterfaceProvider,
    ):
        self.repository = repository
        self.password_hasher = password_hasher

    def execute(self, user: CreateUserSchemaValidation) -> User:
        hashed_password = self.password_hasher.hash(password=user.password)
        new_user = self.repository.create_user(
            CreateUserRepositorySchemaValidation(
                email=user.email,
                password=hashed_password,
            )
        )

        return new_user
