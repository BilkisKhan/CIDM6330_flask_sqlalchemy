import abc
from Flask_SQLAlchemy import models


class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, bookmark: models.BookMarks):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, titles) -> models.BookMarks:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, bookmark):
        print("adding bookmark in thru Repo")
        self.session.add(bookmark)

    def get(self, id):
        return self.session.query(models.BookMarks).filter_by(id=id).one()

    def bookmarklist(self):
        return self.session.query(models.BookMarks).all()
