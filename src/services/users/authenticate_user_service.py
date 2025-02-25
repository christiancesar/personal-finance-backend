from fastapi import HTTPException, status

from providers.jwt.interfaces.jwt_interface_provider import JwtInterfaceProvider
from providers.password_hashed.interfaces.password_hashed_interface_provider import (
    PasswordHasherInterfaceProvider,
)
from repositories.users_repository_interface import UsersRepositoryInterface


class AuthenticateUserService:
    def __init__(
        self,
        user_repository: UsersRepositoryInterface,
        password_hasher: PasswordHasherInterfaceProvider,
        jwt_provider: JwtInterfaceProvider,
    ):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.jwt_provider = jwt_provider

    def execute(self, email: str, password: str) -> str:
        user_exists = self.user_repository.get_user_by_email(email)
        if not user_exists:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        password_match = self.password_hasher.verify(password, user_exists.password)
        if not password_match:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token = self.jwt_provider.encode(user_id=str(user_exists.id))

        return token
