from datetime import datetime
from uuid import UUID, uuid4


class BaseEntity:
    def __init__(self, id: UUID | None = None, updated_at: datetime | None = None):
        self.id = id if id else uuid4()
        self.created_at = datetime.now()
        self.updated_at = None
