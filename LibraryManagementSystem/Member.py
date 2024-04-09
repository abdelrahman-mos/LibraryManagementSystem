import uuid


class Member:
    def __init__(self, name: str):
        self.name = name
        self.id = uuid.uuid4()