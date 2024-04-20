import os
import string
from random import choice

from app import app


def generate_short_name():
    return "".join(choice(string.ascii_letters + string.digits) for _ in range(6))


def save_image(image):
    name = generate_short_name()
    _, extension = image.filename.split(".")
    filename = f"{name}.{extension}"

    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    image.save(path)

    return filename
