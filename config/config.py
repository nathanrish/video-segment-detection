import os

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    DEBUG = FLASK_ENV == 'development'
    TESTING = FLASK_ENV == 'testing'
    DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://user:password@db:5432/database')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'data/videos/')
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}

    @staticmethod
    def is_allowed_file(filename):
        """Check if the file extension is allowed."""
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS