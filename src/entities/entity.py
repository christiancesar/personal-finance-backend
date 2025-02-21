from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4


class BaseEntity:
    def __init__(
        self, id: Optional[UUID] = None, updated_at: Optional[datetime] = None
    ):
        self.id = id if id else uuid4()
        self.created_at = datetime.now()
        self.updated_at = None
