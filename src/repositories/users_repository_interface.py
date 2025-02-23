from abc import ABC, abstractmethod

from pydantic import BaseModel, EmailStr, Field

from entities.user import User


class CreateUserRepositorySchemaValidation(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def create_user(self, user: CreateUserRepositorySchemaValidation) -> User:
        pass
