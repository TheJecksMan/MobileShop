from tests.main_start import client


def test_category():
    response = client.get("/api/caregories/all?page=1&limit=10")
    assert response.status_code == 200


def test_category_parent():
    response = client.get("/api/caregories/parent/73")
    assert response.status_code == 200


def test_product_category():
    response = client.get("/api/caregories/73/product?page=1&limit=1")
    assert response.status_code == 200


def test_category_search():
    response = client.get("/api/caregories/search/%D0%BE%D0%B2?limit=5")
    assert response.status_code == 200
