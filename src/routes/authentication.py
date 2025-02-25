from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from providers.jwt.implementations.py_jwt_provider import PyJwtProvider
from providers.password_hashed.implementations.passlib_bcrypt_provider import (
    PasslibBcryptProvider,
)
from repositories.in_memory.users_repository_in_memory import UsersRepositoryInMemory
from services.users.authenticate_user_service import AuthenticateUserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

authentication_router = APIRouter(prefix="/authentication", tags=["authentication"])

authentication_user_service = AuthenticateUserService(
    user_repository=UsersRepositoryInMemory(),
    password_hasher=PasslibBcryptProvider(),
    jwt_provider=PyJwtProvider(),
)


@authentication_router.post(
    "/",
    name="athentication:create",
)
def authentication(login: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = authentication_user_service.execute(
        email=login.username, password=login.password
    )
    return token
