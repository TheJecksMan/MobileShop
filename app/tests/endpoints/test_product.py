from tests.main_start import client


def test_popular_product():
    response = client.get("/api/product/popular/5")
    assert response.status_code == 200


def test_option_product():
    response = client.get("/api/product/filter/all")
    assert response.status_code == 200


def test_search_product():
    response = client.get("/api/product/search/%D0%BA%D1%80%D0%BE?limit=5")
    assert response.status_code == 200


def test_description_product():
    response = client.get("/api/product/288/description")
    assert response.status_code == 200
    assert response.json() == {
        "description": ""
    }


def test_equipment_product():
    response = client.get("/api/product/equipment/78")
    assert response.status_code == 200


def test_product():
    response = client.get("/api/product/78")
    assert response.status_code == 200
