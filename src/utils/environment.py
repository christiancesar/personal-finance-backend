import os

from dotenv import load_dotenv
from pydantic import BaseModel, Field, ValidationError

load_dotenv()


class Environment(BaseModel):
    JWT_SECRET_KEY: str = Field(min_length=30)
    JWT_ALGORITHM: str = Field(min_length=4)
    HASH_ROUNDS: int = Field(default=1000)
    JWT_EXPIRATION: int = Field(default=3600)
    JWT_LEEWAY: int = Field(default=0)


def validate_environment():
    try:
        Environment(
            JWT_ALGORITHM=os.environ.get("JWT_ALGORITHM"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            HASH_ROUNDS=os.environ.get("HASH_ROUNDS"),
            JWT_EXPIRATION=os.environ.get("JWT_EXPIRATION"),
            JWT_LEEWAY=os.environ.get("JWT_LEEWAY"),
        )

    except ValidationError as exc:
        print(repr(exc.errors()))
        raise Exception(exc.errors())


def get_environment() -> Environment:
    try:
        return Environment(
            JWT_ALGORITHM=os.environ.get("JWT_ALGORITHM"),
            JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
            HASH_ROUNDS=os.environ.get("HASH_ROUNDS"),
            JWT_EXPIRATION=os.environ.get("JWT_EXPIRATION"),
            JWT_LEEWAY=os.environ.get("JWT_LEEWAY"),
        )
    except ValidationError as exc:
        print(repr(exc.errors()))
        raise Exception(exc.errors())
