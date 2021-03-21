"""Application routes."""
from datetime import datetime as dt

from flask import current_app as app
from flask import make_response, redirect, render_template, request, url_for

from .models import BookMarks, db
from flask import Flask, jsonify
import json
from json import JSONEncoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
from Flask_SQLAlchemy import services
from sqlalchemy.orm import mapper, relationship
from Flask_SQLAlchemy import models
from Flask_SQLAlchemy import orm
from Flask_SQLAlchemy import repository


@app.route("/", methods=["GET"])
def addBookMark():

    title = request.args.get("title")
    url = request.args.get("url")
    notes = request.args.get("notes")

    # lines_mapper = mapper(models.BookMarks, orm.flask_bookmarks)

    bookmarkData = BookMarks(
        title=title,
        url=url,
        createdDate=dt.now(),
        notes=notes
    )
    session = db.session

    print("Getting repository object")
    # Call Repository layer
    repo = repository.SqlAlchemyRepository(db.session)
    # Call service layer
    services.BookMarkServices.addBookmark(bookmarkData, repo, session)
    print("completed service layer")
    redirect(url_for("addBookMark"))

    # Call Repository to pull list of bookmarks
    bookmarksList = list(
        repository.SqlAlchemyRepository(db.session).bookmarklist())
    out = json.dumps([to_json(b) for b in bookmarksList], default=str)
    print("done encoding")
    return jsonify(out), 201
    # return render_template("users.jinja2", bookmarksList=BookMarks.query.all(), title="Show BookMarkss")


def to_json(bookmark):

    return {
        'title': bookmark.title,
        'url': bookmark.url,
        'createdDate': bookmark.createdDate,
        'notes': bookmark.notes,
    }
