from sqlalchemy import Column, String, Sequence, Integer

from .base import Base


class Config(Base):
    __tablename__ = "config"
    id = Column('id', Integer, Sequence('config_id_seq'), primary_key=True, autoincrement=True)
    name = Column(String)
    value = Column(String)

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def info(self):
        return {"name": self.name, "value": self.value}
