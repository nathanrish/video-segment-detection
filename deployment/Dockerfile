# Use a lightweight base image with Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]