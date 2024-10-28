from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    # Prepare the new sheep data in a dictionary format.
    new_sheep_data = {
        "id": 7,
        "name": "Margit",
        "breed": "Suffolk",
        "sex": "ewe"
    }

    # Send a POST request to the endpoint "/sheep" with the new sheep data.
    response = client.post("/sheep", json=new_sheep_data)
    # Assert that the response status code is 201
    assert response.status_code == 201
    # Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep_data
    # Verify that the sheep was actually added to the database by retrieving the new sheep by ID.
    get_response = client.get(f"/sheep/{new_sheep_data['id']}")
    assert get_response.status_code == 200
