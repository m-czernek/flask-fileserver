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
# TODO: What does the next command do
python3 -m venv venv
# TODO: What does the next command do
source venv/bin/activate
# TODO: What does the next command do
pip install flask
# TODO: What does the next command do
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
- **Method:** TODO
- **URL:** TODO
- **Body:** TODO
- **Response:** TODO

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
- **Method:** TODO
- **URL:** TODO
- **Response:** TODO

**Example:**
```bash
# TODO
```

#### 4. Rename a File
- **Method:** TODO
- **URL:** TODO
- **Body:** TODO
- **Response:** TODO

**Example:**
```bash
# TODO
# curl can use -d option to specify the payload
# like curl ... -d '{"foo":"bar"}' $url
# it requires application/json content type header
```

**Success Response (200 OK):**
```json
{
  "message": "TODO"
}
```

**Error Response (409 Conflict):**
```json
{
  "error": "TODO"
}
```

#### 5. Delete a File
- **Method:** TODO
- **URL:** TODO
- **Response:** TODO

**Example:**
```bash
# TODO
```

**Success Response (200 OK):**
```json
{
  "message": "TODO"
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "TODO"
}
```

## File Storage

Uploaded files are stored in the `TODO/` directory within the project root. This directory is automatically created when the application starts if it doesn't already exist.

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
