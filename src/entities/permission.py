from uuid import UUID

from entities.entity import BaseEntity
from entities.roles import Roles


class Permission(BaseEntity):
    def __init__(
        self,
        role: Roles,
        resources: dict[str, list[str]],
        id: UUID | None = None,
    ):
        super().__init__(id)
        self.role = role
        self.resources = resources
