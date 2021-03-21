"""Data models."""
from . import db
from dataclasses import dataclass
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship


class BookMarks(db.Model):

    __tablename__ = "flask_bookmarks"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=False,
                      unique=False, nullable=True)
    url = db.Column(db.String(80), index=True, unique=False, nullable=True)
    createdDate = db.Column(db.DateTime, index=False,
                            unique=False, nullable=True)
    notes = db.Column(db.Text, index=False, unique=False, nullable=True)
