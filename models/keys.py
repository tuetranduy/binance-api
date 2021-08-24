from sqlalchemy import Column, String, Sequence, Integer

from .base import Base


class Keys(Base):
    __tablename__ = "keys"
    id = Column('id', Integer, Sequence('key_id_seq'), primary_key=True, autoincrement=True)
    api_key = Column(String)
    secret_key = Column(String)

    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def info(self):
        return {"api_key": self.api_key, "secret_key": self.secret_key}

    def get_api_key(self):
        return self.api_key

    def get_secret_key(self):
        return self.secret_key
