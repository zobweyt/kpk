from statistics import mean
from math import floor

from flask import Blueprint, Response, redirect, render_template, url_for, flash

from app import db
from app.forms import MovieForm, ReviewForm
from app.models import Movie, Review
from app.services import save_image

movies = Blueprint("movies", __name__)


@movies.route("/new/", methods=["GET", "POST"])
def movie_create():
    form = MovieForm()

    if form.validate_on_submit():
        thumbnail = save_image(form.thumbnail.data)

        movie = Movie(
            name=form.name.data,
            genre=form.genre.data,
            plot=form.plot.data,
            release_year=form.release_year.data,
            thumbnail=thumbnail,
        )

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("movies.movie_detail", id=movie.id))

    return render_template("movie-create.html", title="Добавить Фильм", form=form)


@movies.route("/<int:id>/", methods=["GET", "POST"])
def movie_detail(id: int) -> Response:
    review_form = ReviewForm()

    if review_form.validate_on_submit():
        review = Review(
            title=review_form.title.data,
            rating=review_form.rating.data,
            content=review_form.content.data,
            movie_id=id,
        )

        db.session.add(review)
        db.session.commit()

    movie = Movie.query.get(id)
    simular_movies = Movie.query.limit(6).all()
    rating = floor(mean([review.rating for review in movie.reviews] or (0,)))

    return render_template(
        "movie-detail.html",
        title=movie.name,
        movie=movie,
        rating=rating,
        simular_movies=simular_movies,
        review_form=review_form,
    )


@movies.route("/<int:movie_id>/reviews/<int:review_id>/revoke/")
def review_revoke(movie_id: int, review_id: int) -> Response:
    review: Review = Review.query.get(review_id)

    db.session.delete(review)
    db.session.commit()

    movie: Movie = Movie.query.get(movie_id)

    flash("Рецензия была успешно удалена!")
    return redirect(url_for("movies.movie_detail", id=movie.id))
