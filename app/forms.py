from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired, FileSize
from wtforms import FileField, IntegerField, StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class MovieForm(FlaskForm):
    name = StringField(
        "Название",
        validators=[
            DataRequired(),
            Length(max=255),
        ],
    )
    genre = StringField(
        "Жанр",
        validators=[
            DataRequired(),
            Length(max=32),
        ],
    )
    plot = TextAreaField(
        "Сюжет",
        validators=[
            DataRequired(),
            Length(32, 4000),
        ],
        render_kw={"rows": 4},
    )
    release_year = IntegerField("Год релиза")
    thumbnail = FileField(
        "Перетащите обложку сюда",
        validators=[
            FileRequired(),
            FileSize(5_242_880),
            FileAllowed(["png", "jpeg", "jpg", "webp"]),
        ],
    )
    submit = SubmitField("Опубликовать Фильм")


class ReviewForm(FlaskForm):
    title = StringField(
        "Заголовок",
        validators=[
            DataRequired(),
            Length(max=255),
        ],
    )
    content = TextAreaField(
        "Текст",
        validators=[
            DataRequired(),
            Length(max=4000),
        ],
        render_kw={"rows": 4},
    )
    rating = IntegerField("Оценка")
    submit = SubmitField("Опубликовать Рецензию")
