from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='views/templates',
        static_folder='views/static'
    )
    app.config.from_mapping(
        SECRET_KEY='sua_chave_secreta_aqui',
        SQLALCHEMY_DATABASE_URI='sqlite:///../instance/app.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        ENV='production',
        DEBUG=False,
    )

    try:
        app.config.from_pyfile('config.py')
    except FileNotFoundError:
        pass

    db.init_app(app)

    from app.controllers import init_app
    init_app(app)

    with app.app_context():
        if not path.exists('instance/app.db'):
            db.create_all()

    return app
