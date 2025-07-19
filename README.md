Made for the API dev Hackathon!

# Course & Faculty API

A simple FastAPI-based backend for serving course and faculty data from JSON files. Returns pretty-printed JSON for easy reading and testing.

## Features
- List all courses and faculty
- Get a faculty member by ID or by name
- Pretty-printed JSON responses

## Data Structure

### data/courses.json
Each course object contains:
- `id` (int)
- `name` (str)
- `code` (str)
- `description` (str)
- `course_type` (str)
- `credits` (int)
- `department` (str)
- `prerequisites` (list of str)
- `faculty_id` (int)

### data/faculty.json
Each faculty object contains:
- `id` (int)
- `name` (str)
- `email` (str)
- `department` (str)
- `specialization` (list)
- `courses_handled` (list)
- `office_location` (str)
- `office_hours` (str)

## API Endpoints

### Root
- `GET /`
  - Lists available endpoints.

### Courses
- `GET /courses`
  - Returns a list of all courses.

### Faculty
- `GET /faculty`
  - Returns a list of all faculty members.
- `GET /faculty/{faculty_id}`
  - Returns a single faculty member by their ID.
- `GET /faculty/name/{name}`
  - Returns a single faculty member by their name (case-insensitive).

## Usage Examples

### List all courses
```sh
curl http://127.0.0.1:8000/courses
```

### Get a faculty member by ID
```sh
curl http://127.0.0.1:8000/faculty/2
```

### Get a faculty member by name
```sh
curl http://127.0.0.1:8000/faculty/name/Priyanka
```

## Running the Server

1. Install dependencies:
   ```sh
   pip install fastapi uvicorn
   ```
2. Start the server:
   ```sh
   uvicorn main:app --reload
   ```
3. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) or use the endpoints above.

---

**Enjoy exploring your course and faculty data!**
NOTE: THIS DATA IS COMPLETELY MADE UP AND IS NOT REAL!
