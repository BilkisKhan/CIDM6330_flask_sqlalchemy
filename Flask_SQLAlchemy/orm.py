from sqlalchemy import Table, MetaData, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import mapper, relationship

from Flask_SQLAlchemy import models


metadata = MetaData()


flask_bookmarks = Table(
    "flask_bookmarks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, unique=False),
    Column("title", String(255), nullable=True, unique=False),
    Column("url", Integer, nullable=True, unique=False),
    Column("createdDate", Date, nullable=True, unique=False),
    Column("notes", String(255), nullable=True, unique=False)
)
