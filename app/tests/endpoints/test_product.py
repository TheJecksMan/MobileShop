"""TestClient"""
from httpx import AsyncClient
from tests.main_start import BASE_URL, appTest, anyio_backend


async def test_popular_product(anyio_backend):
    """Тестирование получения самых просматриваемых продуктов"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/product/popular/5")
        response_uncorrect_params = await client.get("/api/product/popular/-5")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 400


async def test_option_product(anyio_backend):
    """Получение информации о продуктах"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_without_params = await client.get("/api/product/filter/all")

    assert response_without_params.status_code == 200


async def test_search_product(anyio_backend):
    """Тестирование поиска товара"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/product/search/%D0%BA%D1%80%D0%BE?limit=5")
        response_uncorrect_params = await client.get("/api/product/search/%D0%BA%D1%80%D0%BE?limit=-5")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 400


async def test_description_product(anyio_backend):
    """Тестирование получения описания товара"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/product/288/description")
        response_uncorrect_params = await client.get("/api/product/-288/description")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 404


async def test_equipment_product(anyio_backend):
    """Тестирование полученнной комплектации товара"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/product/equipment/78")
        response_uncorrect_params = await client.get("/api/product/equipment/-78")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 200
    assert response_uncorrect_params.json() == []


async def test_get_product(anyio_backend):
    """Тестирование получения базовой информации о продукте"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/product/78")
        response_with_hiden_items = await client.get("/api/product/87")
        response_uncorrect_params = await client.get("/api/product/-78")

    assert response_with_params.status_code == 200
    assert response_with_hiden_items.status_code == 404
    assert response_uncorrect_params.status_code == 404


async def test_product_multiple(anyio_backend):
    """Тестирование получение информации о нескольких товарах"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.post("/api/product/multiple", json={"ids": [66, 67]})
        response_without_params = await client.post("/api/product/multiple", json={"ids": []})
        response_uncorrect_params = await client.post("/api/product/multiple")

    assert response_without_params.status_code == 404
    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 422
