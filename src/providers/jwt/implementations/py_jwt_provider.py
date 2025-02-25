from datetime import datetime, timedelta
from typing import Dict

import jwt

from providers.jwt.interfaces.jwt_interface_provider import JwtInterfaceProvider
from utils.environment import get_environment


class PyJwtProvider(JwtInterfaceProvider):
    def encode(self, user_id: str) -> str:
        expire = datetime.now() + timedelta(
            milliseconds=get_environment().JWT_EXPIRATION
        )
        payload = {"sub": user_id, "exp": expire}

        token = jwt.encode(  # type: ignore
            payload=payload,
            key=get_environment().JWT_SECRET_KEY,
            algorithm=get_environment().JWT_ALGORITHM,
        )
        return token

    def decode(self, token: str) -> str | None:
        payload: Dict[str, str] = jwt.decode(  # type: ignore
            jwt=token,
            key=get_environment().JWT_SECRET_KEY,
            algorithms=[get_environment().JWT_ALGORITHM],
            leeway=get_environment().JWT_LEEWAY,
        )

        userId = payload.get("sub")
        return userId
