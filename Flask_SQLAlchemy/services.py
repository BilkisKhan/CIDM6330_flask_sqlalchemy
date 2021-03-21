from __future__ import annotations

from Flask_SQLAlchemy import models
from Flask_SQLAlchemy import repository


class BookMarkServices:
    pass

    def addBookmark(bookmarkData: bookmark, repo: AbstractRepository, session) -> str:

        repository.SqlAlchemyRepository(session).add(bookmarkData)
        # Commits all changes
        session.commit()
        return "added"
