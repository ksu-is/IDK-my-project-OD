"""
Soccer Practice Planner - A web app for creating customized soccer practice sessions
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soccer_planner.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Register routes
    from app import routes
    app.register_blueprint(routes.bp)

    # Create database tables
    with app.app_context():
        db.create_all()

    return app
