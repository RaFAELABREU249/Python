from app.controllers.auth import bp as auth_bp
from app.controllers.tasks import bp as tasks_bp
from app.controllers.api import bp as api_bp


def init_app(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(api_bp)
