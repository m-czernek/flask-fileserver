import os
from flask import Blueprint, request, jsonify, send_from_directory, render_template, current_app
from werkzeug.utils import secure_filename

files_bp = Blueprint('files', __name__)


# --- WEB UI ROUTE ---

@files_bp.route('/')
def index():
    return render_template('index.html')


# --- API ENDPOINTS ---

# 1. Upload a new file
@files_bp.route('/files', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request payload"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected for uploading"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(filepath):
        return jsonify({"error": f"File '{filename}' already exists. Use PUT to rename or delete it first."}), 409

    try:
        file.save(filepath)
        return jsonify({"message": f"File '{filename}' uploaded successfully"}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to save file: {str(e)}"}), 500


# 2. List all stored files
@files_bp.route('/files', methods=['GET'])
def list_files():
    try:
        files = [
            f for f in os.listdir(current_app.config['UPLOAD_FOLDER'])
            if os.path.isfile(os.path.join(current_app.config['UPLOAD_FOLDER'], f))
        ]
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to list files: {str(e)}"}), 500


# 3. Serve/Download a particular file
@files_bp.route('/files/<filename>', methods=['GET'])
def download_file(filename):
    filename = secure_filename(filename)
    try:
        return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        return jsonify({"error": f"File '{filename}' not found"}), 404


# 4. Update the filename of a particular file
@files_bp.route('/files/<filename>', methods=['PUT'])
def rename_file(filename):
    filename = secure_filename(filename)
    old_filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    if not os.path.exists(old_filepath) or not os.path.isfile(old_filepath):
        return jsonify({"error": f"File '{filename}' not found"}), 404

    data = request.get_json()
    if not data or 'new_filename' not in data:
        return jsonify({"error": "Missing 'new_filename' parameter in JSON body"}), 400

    new_filename = secure_filename(data['new_filename'])
    if not new_filename:
        return jsonify({"error": "Invalid target filename"}), 400

    new_filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename)

    if os.path.exists(new_filepath):
        return jsonify({"error": f"A file named '{new_filename}' already exists"}), 409

    try:
        os.rename(old_filepath, new_filepath)
        return jsonify({"message": f"File successfully renamed from '{filename}' to '{new_filename}'"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to rename file: {str(e)}"}), 500


# 5. Delete a particular file
@files_bp.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(filepath) and os.path.isfile(filepath):
        try:
            os.remove(filepath)
            return jsonify({"message": f"File '{filename}' deleted successfully"}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to delete file: {str(e)}"}), 500

    return jsonify({"error": f"File '{filename}' not found"}), 404
