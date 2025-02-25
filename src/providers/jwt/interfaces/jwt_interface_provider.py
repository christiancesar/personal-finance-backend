from abc import ABC, abstractmethod


class JwtInterfaceProvider(ABC):
    @abstractmethod
    def encode(self, user_id: str) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> str | None:
        pass
