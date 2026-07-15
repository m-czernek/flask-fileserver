# Flask File Manager

A simple Flask-based file management application with a clean web UI and RESTful API endpoints.

## Project Structure

```
.
├── app.py                 # Flask application entry point
├── routes.py              # Blueprint with all endpoints
├── templates/
│   └── index.html         # Web UI template
├── uploads/               # Directory for storing uploaded files
└── README.md              # This file
```

## Running the Application

To run the application, execute:

```bash
# Create a Python virtual environment 
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install dependencies
pip install flask
# Start the application
python3 app.py
```

### API Endpoints

All endpoints are prefixed with `/files` and handle JSON responses.

#### 1. List All Files
- **Method:** `GET`
- **URL:** `http://127.0.0.1:5000/files`
- **Response:** JSON array of filenames

**Example:**
```bash
curl http://127.0.0.1:5000/files
```

**Response:**
```json
{
  "files": ["document.pdf", "image.png", "data.xlsx"]
}
```

#### 2. Upload a File
- **Method:** `POST`
- **URL:** `http://127.0.0.1:5000/files`
- **Body:** Multipart form data with key `file` containing the file
- **Response:** Success message or error

**Example:**
```bash
curl -X POST -F "file=@/path/to/file.txt" http://127.0.0.1:5000/files
```

**Success Response (201 Created):**
```json
{
  "message": "File 'file.txt' uploaded successfully"
}
```

**Error Response (409 Conflict):**
```json
{
  "error": "File 'file.txt' already exists. Use PUT to rename or delete it first."
}
```

#### 3. Download a File
- **Method:** `GET`
- **URL:** `http://127.0.0.1:5000/files/<filename>`
- **Response:** File content as attachment

**Example:**
```bash
curl -O http://127.0.0.1:5000/files/document.pdf
```

#### 4. Rename a File
- **Method:** `PUT`
- **URL:** `http://127.0.0.1:5000/files/<filename>`
- **Body:** JSON with `new_filename` key
- **Response:** Success message or error

**Example:**
```bash
curl -X PUT -H "Content-Type: application/json" \
  -d '{"new_filename":"new_name.txt"}' \
  http://127.0.0.1:5000/files/old_name.txt
```

**Success Response (200 OK):**
```json
{
  "message": "File successfully renamed from 'old_name.txt' to 'new_name.txt'"
}
```

**Error Response (409 Conflict):**
```json
{
  "error": "A file named 'new_name.txt' already exists"
}
```

#### 5. Delete a File
- **Method:** `DELETE`
- **URL:** `http://127.0.0.1:5000/files/<filename>`
- **Response:** Success message or error

**Example:**
```bash
curl -X DELETE http://127.0.0.1:5000/files/document.pdf
```

**Success Response (200 OK):**
```json
{
  "message": "File 'document.pdf' deleted successfully"
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "File 'document.pdf' not found"
}
```

## File Storage

Uploaded files are stored in the `uploads/` directory within the project root. This directory is automatically created when the application starts if it doesn't already exist.

## Error Handling

The API provides appropriate HTTP status codes:

- **201 Created:** File uploaded successfully
- **200 OK:** Operation completed successfully
- **400 Bad Request:** Invalid request (missing parameters, empty filename, etc.)
- **404 Not Found:** File not found
- **409 Conflict:** File already exists
- **500 Internal Server Error:** Server-side error


## Technologies Used

- **Flask:** Lightweight Python web framework
- **Werkzeug:** WSGI utilities for filename sanitization
- **Tailwind CSS:** Modern CSS framework for UI styling

## License

This project is open source and available under the MIT License.
