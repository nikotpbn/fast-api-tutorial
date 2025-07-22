from fastapi.testclient import TestClient

from .main import app
from .models import Item

client = TestClient(app)


def test_item_create():
    data = {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5,
    }
    response = client.post(
        "/items/",
        json=data,
    )

    assert response.status_code == 200
    assert response.json() == data
