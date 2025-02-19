from uuid import UUID, uuid4


class Bank:
    def __init__(self, ispb: str, name: str, code: int, fullName: str, id: UUID = None):
        self.id = id if id else uuid4()
        self.name = name
        self.ispb = ispb
        self.code = code
        self.fullName = fullName
