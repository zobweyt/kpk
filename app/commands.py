import click

from app import app, db
from app.models import User
from werkzeug.security import generate_password_hash


@app.cli.command("create-superuser")
@click.argument("username")
@click.argument("password")
@click.argument("email")
def create_superuser(username: str, password: str, email: str):
    user = User(
        username=username,
        password=generate_password_hash(password, method="scrypt"),
        email=email,
        is_staff=True,
        is_superuser=True,
    )
    db.session.add(user)
    db.session.commit()
