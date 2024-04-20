from flask import (
    Blueprint,
    Response,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
from app.models import User

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login() -> str:
    return render_template("auth/login.html")


@auth.route("/login", methods=["POST"])
def login_post() -> Response:
    username = request.form.get("username")
    password = request.form.get("password")

    user: User = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        flash("Неверный логин или пароль.")
        return redirect(url_for("auth.login"))

    login_user(user, remember=True)
    return redirect(url_for("index"))


@auth.route("/signup")
def signup() -> str:
    return render_template("auth/signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post() -> Response:
    email: str = request.form.get("email")
    username: str = request.form.get("username")
    password: str = request.form.get("password")

    user: User = User.query.filter_by(email=email).first()

    if user:
        flash("Такой пользователь уже существует.")
        return redirect(url_for("auth.signup"))

    new_user: User = User(
        email=email,
        username=username,
        password=generate_password_hash(password, method="scrypt"),
        is_staff=False,
        is_superuser=False,
    )

    db.session.add(new_user)
    db.session.commit()

    login_user(new_user, remember=True)
    return redirect(url_for("index"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/users")
def users() -> str:
    if not current_user.is_superuser:
        return redirect(url_for("index"))
    users = User.query.all()
    return render_template("auth/users.html", users=users)


@auth.route("/users", methods=["POST"])
def users_post() -> Response:
    checked_user_ids = request.form.getlist("user_ids[]")
    checked_user_ids = [int(id) for id in checked_user_ids]

    User.query.update({"is_staff": False})
    User.query.filter(User.id.in_(checked_user_ids)).update(
        {"is_staff": True}, synchronize_session=False
    )
    db.session.commit()

    flash("Список был успешно обновлён!")
    return redirect(url_for("auth.users"))
