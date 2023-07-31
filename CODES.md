# CODES

## Codes to build the image and run the Dockerfile locally

"""
docker build -t rest-apis-flask-python-3 .
"""

"""
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" rest-apis-flask-python-3 sh -c "flask run --host 0.0.0.0"
"""