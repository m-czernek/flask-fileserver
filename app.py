import os
from flask import Flask
from routes import files_bp

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Register blueprint containing all routes
app.register_blueprint(files_bp)

if __name__ == '__main__':
    app.run()
