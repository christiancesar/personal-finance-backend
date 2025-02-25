from fastapi import APIRouter
from pydantic import BaseModel, EmailStr, Field

from presenters.user_presenter import UserPresenter
from providers.password_hashed.implementations.passlib_bcrypt_provider import (
    PasslibBcryptProvider,
)
from repositories.in_memory.users_repository_in_memory import UsersRepositoryInMemory
from services.users.create_user_service import (
    CreateUserService,
)

users_router = APIRouter(prefix="/users", tags=["users"])

user_repository = UsersRepositoryInMemory()
password_hasher_provider = PasslibBcryptProvider()

create_user_service = CreateUserService(
    repository=user_repository, password_hasher=password_hasher_provider
)


class CreateUserRequestBody(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


@users_router.post(
    "/",
    name="users:create",
    response_model=UserPresenter,
)
def create_user(user: CreateUserRequestBody) -> UserPresenter:
    new_user = create_user_service.execute(**user.model_dump())
    return new_user  # type: ignore
