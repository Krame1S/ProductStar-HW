from typing import Optional, List
import uuid
from app.data.product_repo import save, get_by_id, get_many
from app.model.product import Product

def product_create(name: str, price: float) -> Product:
    product = Product(
        id=str(uuid.uuid4()),
        name=name,
        price=price,
    )
    save(product)
    return product

def product_get_by_id(id: str) -> Optional[Product]:
    return get_by_id(id)

def product_get_many(page: int, limit: int) -> List[Product]:
    return get_many(page=page, limit=limit)