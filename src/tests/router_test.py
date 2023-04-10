from fastapi.testclient import TestClient
from src.api.routers import router

client = TestClient(router)


def test_predict_lung_post_success():
    body = {
        "age": 62,
        "alcohol_consuming": True,
        "wheezing": True,
        "allergy": False,
        "chest_pain": False
    }

    response = client.post(
        "/v1/predict",
        json=body
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Successfully predict the lung cancer person",
        "is_lung_cancer": True
    }


def test_predict_lung_post_failed():
    body = {
        "age": 10,
        "alcohol_consuming": False,
        "wheezing": False,
        "allergy": False,
        "chest_pain": False
    }

    response = client.post(
        "/v1/predict",
        json=body
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Successfully predict the lung cancer person",
        "is_lung_cancer": False
    }
