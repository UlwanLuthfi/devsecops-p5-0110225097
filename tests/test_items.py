from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "inventory-api"}


def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2


def test_get_item_by_id():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_create_item():
    payload = {
        "name": "Hardware Wallet",
        "description": "Cold storage crypto wallet",
        "price": 99.99,
        "status": "available",
    }
    response = client.post("/items", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Hardware Wallet"
    assert "id" in data


def test_get_nonexistent_item():
    response = client.get("/items/9999")
    assert response.status_code == 404
