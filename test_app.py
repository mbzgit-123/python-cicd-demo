from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    # assert response.json()["message"] == "Hello CI/CD!"
    assert response.json()["message"] == "我是错误内容"


def test_hello():
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json()["message"] == "Hello Agent!"
