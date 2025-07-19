from fastapi import FastAPI
import json
import os
from fastapi.responses import JSONResponse
from fastapi import Response

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_json(filename):
    with open(os.path.join(BASE_DIR, "data", filename), "r") as f:
        return json.load(f)

@app.get("/")
def root():
    return Response(
        content=json.dumps({
        "available_endpoints": {
            "courses": "/courses",
            "course by id": "/courses/{course_id}",
            "faculty": "/faculty",
            "faculty by id": "/faculty/{faculty_id}",
            "faculty by name": "/faculty/name/{name}",
            "all names": "/all-names"
        },
        "Interactive API": "http://127.0.0.1:8000/docs#/",
        "Code and Documentation": "https://github.com/vvvv5215/api-dev-hackathon"
    },
    indent=2),
    media_type= "application/json")


@app.get("/courses")
def get_courses():
    data = load_json("courses.json")
    pretty = json.dumps(data, indent=2)
    return Response(content=pretty, media_type="application/json")

@app.get("/faculty")
def get_faculty():
    data = load_json("faculty.json")
    pretty = json.dumps(data, indent=2)
    return Response(content=pretty, media_type="application/json")

@app.get("/faculty/{faculty_id}")
def get_faculty_by_id(faculty_id: int):
    data = load_json("faculty.json")
    for faculty in data:
        if faculty["id"] == faculty_id:
            pretty = json.dumps(faculty, indent=2)
            return Response(content=pretty, media_type="application/json")
    return Response(content=json.dumps({"error": "Faculty not found"}, indent=2), media_type="application/json", status_code=404)

@app.get("/faculty/name/{name}")
def get_faculty_by_name(name: str):
    data = load_json("faculty.json")
    for faculty in data:
        if faculty["name"].lower() == name.lower():
            pretty = json.dumps(faculty, indent=2)
            return Response(content=pretty, media_type="application/json")
    return Response(content=json.dumps({"error": "Faculty not found"}, indent=2), media_type="application/json", status_code=404)

@app.get("/all-names")
def get_all_names():
    courses = load_json("courses.json")
    faculty = load_json("faculty.json")
    course_names = [course["name"] for course in courses]
    faculty_names = [f["name"] for f in faculty]
    result = {"courses": course_names, "faculty": faculty_names}
    pretty = json.dumps(result, indent=2)
    return Response(content=pretty, media_type="application/json")

@app.get("/courses/{course_id}")
def get_courses_by_id(course_id: int):
    data = load_json("courses.json")
    for faculty in data:
        if faculty["id"] == course_id:
            pretty = json.dumps(faculty, indent=2)
            return Response(content=pretty, media_type="application/json")
    return Response(content=json.dumps({"error": "Faculty not found"}, indent=2), media_type="application/json", status_code=404)
