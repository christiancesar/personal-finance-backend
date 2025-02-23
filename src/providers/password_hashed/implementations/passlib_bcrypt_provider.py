from passlib.context import CryptContext

from providers.password_hashed.interfaces.password_hashed_interface_provider import (
    PasswordHasherInterfaceProvider,
)
from utils.environment import get_environment


class PasslibBcryptProvider(PasswordHasherInterfaceProvider):
    def __init__(self):
        self.__crypt_context = CryptContext(
            schemes="sha256_crypt",
            sha256_crypt__default_rounds=get_environment().HASH_ROUNDS,
        )

    def hash(self, password: str) -> str:
        return self.__crypt_context.hash(password)

    def verify(self, password: str, hash: str) -> bool:
        return self.__crypt_context.verify(password, hash)
