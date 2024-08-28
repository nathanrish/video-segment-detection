from flask import Flask
from config.config import Config
from app.routes import routes
import logging.config

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Load logging configuration
    logging.config.fileConfig('config/logging.conf')
    
    # Register the routes Blueprint
    app.register_blueprint(routes)

    return app