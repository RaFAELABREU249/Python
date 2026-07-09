from flask import Flask

from models import db
from controllers import calculadora_bp


def create_app():
    app = Flask(
        __name__,
        static_folder="views/static",
        template_folder="views/templates",
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calculadora.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(calculadora_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
