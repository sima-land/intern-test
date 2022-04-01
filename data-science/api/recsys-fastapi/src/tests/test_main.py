from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_train():
    response = client.get("/train")
    assert response.status_code == 200
    assert response.json() == {"message": "Model built"}


def test_get_user_recommendations_success():
    response = client.get("/api/get_user_recommendations/721985")
    data = response.json()
    assert response.status_code == 200
    assert len(data["recommendations"]) == 10


def test_get_user_recommendations_fail():
    response = client.get("/api/get_user_recommendations/1234567")
    assert response.status_code == 404
