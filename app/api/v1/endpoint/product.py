"""
API implementation module for product.
/api/product
"""
from typing import Any
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from modules.database.deps import get_session

from modules.database.plugins.orm import orm_product
from modules.database.plugins.scheme import scheme_product as scheme


router = APIRouter()


@router.get("/{product_id}", response_model=scheme.AdvancedDetailProduct)
async def get_detail_product(
    product_id: int,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Getting basic information about the product.
    """
    base_product = await orm_product.get_product_by_id(product_id, db_session)
    base_desc = await orm_product.get_product_description_by_id(product_id, db_session)

    desc = scheme.DetailProduct(
        product_id=base_product.product_id,
        model=base_product.model,
        image=base_product.image,
        price=base_product.price,
        quantity=base_product.quantity,
        name=base_product.name,
        description=base_desc.description
    )
    return scheme.AdvancedDetailProduct(item=desc)


@router.get("/equipment/{product_id}", response_model=list[scheme.BaseProductEquipment])
async def get_equipment_product(
        product_id: int,
        db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Obtaining information about the available configuration of the goods
    """
    equipment = await orm_product.get_equipment(product_id, db_session)
    return equipment


@router.post('/multiple', response_model=scheme.AdvancedMultipleProduct)
async def get_detail_multiple_products(
    multiple_product: scheme.MultipleProduct,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Getting basic data about several products.
    ---
    Input limit up to 30 list values
    """
    product = await orm_product.get_multiple_product_by_id(multiple_product.ids, db_session)
    return scheme.AdvancedMultipleProduct(items=product)


@router.get("/{product_id}/description", response_model=scheme.DescProduct)
async def get_product_description(
    product_id: int,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Getting a detailed product description
    """
    product = await orm_product.get_product_description_by_id(product_id, db_session)
    return product


@router.get("/page/{page}", response_model=list[scheme.BaseProductCategory])
async def get_product_category(
    page: int,
    limit: int = 10,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Getting a list of all products"""
    product = await orm_product.get_all_product(page, limit, db_session)
    return product


@router.get("/search/{search_text}", response_model=scheme.AdvancedSearchProduct)
async def product_search(
    search_text: str,
    page: int = 1, limit: int = 5,
    category_id: int = None,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """Product search by product name.
    You can search for products in a specific category
    """
    product = await orm_product.search_product(category_id, search_text, page, limit, db_session)
    return scheme.AdvancedSearchProduct(items=product)


@router.get("/popular/{limit}", response_model=scheme.AdvancedPopularProduct)
async def get_popular_product(
    limit: int,
    db_session: AsyncSession = Depends(get_session)
) -> Any:
    """List of most viewed products.
    """
    product = await orm_product.get_popular_product(limit, db_session)
    return scheme.AdvancedPopularProduct(items=product)


@router.get("/filter/all", response_model=scheme.FilterGeneral)
async def get_all_param_filter(db_session: AsyncSession = Depends(get_session)) -> Any:
    """Obtaining a complete list of available parameters for further filtering
    """
    params, option = await orm_product.get_params_option(db_session)

    return scheme.FilterGeneral(items=params, option=option)
