from flask import Flask
from controllers.cinema_controller import cinema_bp
from controllers.dashboard_controller import dashboard_bp
from models import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cinema.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Register blueprints
app.register_blueprint(cinema_bp)
app.register_blueprint(dashboard_bp)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()