from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session
from sqlalchemy.util.compat import contextmanager

from models.base import Base
from models.keys import Keys

dbschema = 'binancebot'


class Database:
    def __init__(self,
                 uri="postgresql+psycopg2://pecjlwcreqdavo"
                     ":3c9542654598a23aff7a82bc7d72057b9de80b4d77380517de65b4ce946da34c@ec2-52-45-179-101.compute-1"
                     ".amazonaws.com:5432/d8d9q7u65kchn7"):
        self.engine = create_engine(uri, connect_args={'options': '-csearch_path={}'.format(dbschema)})
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
