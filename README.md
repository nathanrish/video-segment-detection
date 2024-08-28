
# Video Segment Detection

## Overview

The Video Segment Detection project provides a web application to analyze and detect different segments within videos, such as bars & tones, program slates, black frames, and other textless elements. It uses a TimesFormer model for video classification and segmentation. This guide will help you set up and use the application.

## Project Structure

```
video-segment-detection/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── static/
│   └── templates/
│       ├── index.html
│       └── results.html
├── config/
│   ├── config.py
│   └── logging.conf
├── data/
│   ├── annotations/
│   ├── frames/
│   ├── models/
│   ├── videos/
│   └── audio/
├── deployment/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── cloud/
├── scripts/
│   ├── data_preparation.py
│   ├── train_timesformer.py
│   ├── detection_pipeline.py
│   └── evaluate_model.py
├── tests/
│   ├── test_data_preparation.py
│   ├── test_detection_pipeline.py
│   ├── test_flask_app.py
│   └── test_model_training.py
├── .gitignore
└── app.py
```

## Prerequisites

- Python 3.7 or later
- Pip (Python package manager)
- Git
- Docker (for deployment)

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/nathanrish/video-segment-detection.git
cd video-segment-detection
```

### Install Dependencies

1. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Configure Logging

1. **Edit `config/logging.conf` to configure logging settings as needed.**

### Run the Application

1. **Start the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the web application:**

   Open a web browser and go to `http://127.0.0.1:5000`.

## Usage

1. **Upload a video:**

   On the home page, use the file upload form to select and upload a video file.

2. **View results:**

   After uploading, the application processes the video and displays the detection results on a results page.

## Development

### Running Tests

To run tests, ensure the virtual environment is activated and use:

```bash
pytest
```

### Docker Deployment

1. **Build Docker image:**

   ```bash
   docker build -t video-segment-detection .
   ```

2. **Run Docker container:**

   ```bash
   docker run -p 5000:5000 video-segment-detection
   ```

3. **Or use Docker Compose for multi-container deployment:**

   ```bash
   docker-compose up
   ```

## Configuration

- **`config/config.py`**: Configuration settings for the application.
- **`config/logging.conf`**: Configuration file for logging.

## Contributing

1. **Fork the repository.**
2. **Create a new branch for your changes:**

   ```bash
   git checkout -b my-feature-branch
   ```

3. **Commit your changes:**

   ```bash
   git commit -am 'Add new feature'
   ```

4. **Push to the branch:**

   ```bash
   git push origin my-feature-branch
   ```

5. **Create a pull request on GitHub.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **TimesFormer**: A model used for video classification and segmentation.

Feel free to reach out for any questions or clarifications. Happy coding!


