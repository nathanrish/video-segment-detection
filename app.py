from flask import Flask
from config.config import Config
from app.routes import routes

def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Register the routes Blueprint
    app.register_blueprint(routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)