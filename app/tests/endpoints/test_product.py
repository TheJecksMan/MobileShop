"""TestClient"""
from tests.main_start import client


def test_popular_product():
    """Тестирование получения самых просматриваемых продуктов"""
    response = client.get("/api/product/popular/5")
    assert response.status_code == 200


def test_option_product():
    """Получение информации о продуктах"""
    response = client.get("/api/product/filter/all")
    assert response.status_code == 200


def test_search_product():
    """Тестирование поиска товара"""
    response = client.get("/api/product/search/%D0%BA%D1%80%D0%BE?limit=5")
    assert response.status_code == 200


def test_description_product():
    """Тестирование получения описания товара"""
    response = client.get("/api/product/288/description")
    assert response.status_code == 200


def test_equipment_product():
    """Тестирование полученнной комплектации товара"""
    response = client.get("/api/product/equipment/78")
    assert response.status_code == 200


def test_product():
    """Тестирование получения базовой информации о продукте"""
    response = client.get("/api/product/78")
    assert response.status_code == 200
