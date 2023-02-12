"""TestClient"""
from httpx import AsyncClient
from tests.main_start import BASE_URL, appTest, anyio_backend


async def test_category(anyio_backend):
    """Тестирование получения самых просматриваемых продуктов"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/caregories/all?page=1&limit=10")
        response_without_params = await client.get("/api/caregories/all")
        response_uncorrect_params = await client.get("/api/caregories/all?page=1345f&limit=53dfrg")

    assert response_with_params.status_code == 200
    assert response_without_params.status_code == 200
    assert response_uncorrect_params.status_code == 422


async def test_category_parent(anyio_backend):
    """Тестирование получение подгатегории"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("api/caregories/parent/65")
        response_uncorrect_params = await client.get("api/caregories/parent/65d")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 422


async def test_product_category(anyio_backend):
    """Тестирование получение товаров по категориям"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/caregories/65/product?page=1&limit=1")
        response_without_params = await client.get("/api/caregories/65/product")
        response_uncorrect_params = await client.get("/api/caregories/65/product?page=1fdge&limit=1fdg")

    assert response_with_params.status_code == 200
    assert response_without_params.status_code == 422
    assert response_uncorrect_params.status_code == 422


async def test_category_search(anyio_backend):
    """Тестирование поиска категорий"""
    async with AsyncClient(app=appTest, base_url=BASE_URL) as client:
        response_with_params = await client.get("/api/caregories/search/%D0%BE%D0%B2?limit=5")
        response_uncorrect_params = await client.get("/api/caregories/search/%D0%BE%D0%B2?limit=-5")

    assert response_with_params.status_code == 200
    assert response_uncorrect_params.status_code == 400
