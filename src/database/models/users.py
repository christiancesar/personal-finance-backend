from uuid import uuid4

from sqlmodel import Field, SQLModel  # type: ignore


class User(SQLModel, table=True):
    id: str = Field(default_factory=uuid4, primary_key=True)
    email: str = Field(unique=True)
    password: str = Field(min_length=8)
    # roles: List[Roles]
    disabled: bool = Field(default=False)
    # profile: Profile | None = None
    # account: Account | None = None
