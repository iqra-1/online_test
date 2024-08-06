import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_create_user(client):
    # Check if the user already exists
    response = client.get("/users/testuser")
    if response.status_code == 404:
        response = client.post(
            "/users/", json={"username": "testuser", "password": "testpass"}
        )
        assert response.status_code == 200
    else:
        assert response.status_code == 200


def test_create_test(client):
    response = client.post(
        "/tests/", json={"title": "Test 1", "description": "Description of Test 1"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test 1"


def test_create_question(client):
    response = client.post("/questions/", json={"text": "Question 1", "test_id": 1})
    assert response.status_code == 200
    assert response.json()["text"] == "Question 1"


def test_create_answer(client):
    response = client.post(
        "/answers/", json={"text": "Answer 1", "is_correct": True, "question_id": 1}
    )
    assert response.status_code == 200
    assert response.json()["text"] == "Answer 1"


def test_get_test_results(client):
    # Create a user if not exists
    response = client.post(
        "/users/", json={"username": "testuser", "password": "testpass"}
    )
    if response.status_code == 400:
        response = client.get("/users/testuser")
        assert response.status_code == 200
        user_id = response.json()["id"]
    else:
        assert response.status_code == 200
        user_id = response.json()["id"]

    # Create a test result if not exists
    response = client.post(
        "/results/",
        json={
            "test_id": 1,
            "user_id": user_id,
            "score": 85.0,
            "total_questions": 10,
            "correct_answers": 8,
        },
    )
    if response.status_code == 400:
        response = client.get(f"/tests/1/results/")
        assert response.status_code == 200
    else:
        assert response.status_code == 200

    # Retrieve the test results
    response = client.get("/tests/1/results/")
    assert response.status_code == 200
    assert response.json() == {
        "test_id": 1,
        "user_id": user_id,
        "score": 85.0,
        "total_questions": 10,
        "correct_answers": 8,
    }
