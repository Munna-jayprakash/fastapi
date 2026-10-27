from fastapi.testclient import TestClient
from main import app, students

client = TestClient(app)


def setup_function():
    students.clear()


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_add_student():
    response = client.post(
        "/students",
        json={
            "name": "MUNNA",
            "roll_no": "MCA024",
            "marks": 90,
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "MUNNA"


def test_invalid_marks():
    response = client.post(
        "/students",
        json={
            "name": "Meera",
            "roll_no": "MCA102",
            "marks": 150,
        },
    )

    assert response.status_code == 422