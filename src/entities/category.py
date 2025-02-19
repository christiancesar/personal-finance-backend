from uuid import UUID, uuid4


class Category:
    def __init__(self, name: str, id: UUID = None):
        self.id = id if id else uuid4()
        self.name = name
