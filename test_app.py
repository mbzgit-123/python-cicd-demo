import os
from fastapi.testclient import TestClient

from app import app

# 创建测试客户端
client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_home_message():
    response = client.get("/")
    assert response.json()["message"] == "Hello CI/CD!"


def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200


def test_hello_message():
    response = client.get("/hello")
    assert response.json()["message"] == "Hello Agent!"
