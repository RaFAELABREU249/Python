from flask import Blueprint

bp = Blueprint('tasks', __name__)

from app.controllers.tasks import routes  # noqa: F401
