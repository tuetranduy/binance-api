from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.util.compat import contextmanager

from models.base import Base
from models.keys import Keys


class Database:
    def __init__(self, uri="sqlite:////database/data.db"):
        self.engine = create_engine(uri)
        self.SessionMaker = sessionmaker(bind=self.engine)

    @contextmanager
    def db_session(self):
        session: Session = scoped_session(self.SessionMaker)
        yield session
        session.commit()
        session.close()

    def create_database(self):
        Base.metadata.create_all(self.engine)

    def set_keys(self, keys):
        session: Session
        with self.db_session() as session:
            session.add(keys)

    def get_keys(self):
        session: Session
        with self.db_session() as session:
            keys = session.query(Keys).order_by(Keys.id.desc()).first()
            session.expunge(keys)
            return keys


if __name__ == "__main__":
    database = Database()
    database.create_database()
