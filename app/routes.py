from flask import Blueprint, render_template, request
from detection_pipeline import detect_elements
from models import load_model
import os
from config.config import Config

# Create a blueprint for the routes
routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No file part", 400

    video_file = request.files['video']

    if video_file.filename == '':
        return "No selected file", 400

    if video_file:
        # Save the uploaded video
        video_path = os.path.join(Config.UPLOAD_FOLDER, video_file.filename)
        video_file.save(video_path)

        # Load the pre-trained TimesFormer model
        model = load_model('data/models/timesformer')

        # Process the video and get detection results
        results = detect_elements(model, video_path)

        return render_template('results.html', results=results)