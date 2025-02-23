from uuid import UUID

from .entity import BaseEntity


class Profile(BaseEntity):
    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        id: UUID | None = None,
    ):
        super().__init__(id)
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = "{} {}".format(self.first_name, self.last_name)
        self.email = email
        self.phone = phone
