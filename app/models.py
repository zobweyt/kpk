from datetime import datetime
from flask_login import UserMixin

from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_staff = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.now)


@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


class Review(db.Model):
    __tablename__ = "reviews"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(length=4000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    movie = db.relationship("Movie", back_populates="reviews")

    def __repr__(self):
        return self.id


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    plot = db.Column(db.Text(length=4000), nullable=False)
    thumbnail = db.Column(db.String, nullable=False)
    reviews = db.relationship("Review", back_populates="movie")

    def __repr__(self):
        return self.name
