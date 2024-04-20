from flask import render_template, send_from_directory

from app import app
from app.models import Movie


@app.get("/media/<path:path>")
def media(path):
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path=path)


@app.route("/")
def index():
    movies = Movie.query.order_by(Movie.id.desc()).all()
    return render_template("index.html", movies=movies)
