from typing import List
import uuid
from data.order_repo import get_by_id, get_many, save
from model.order import Order
from data.product_repo import get_by_id as product_get_by_id

def order_create(product_ids: List[str]) -> Order:
    products = []
    for id in product_ids:
        product = product_get_by_id(id)
        if product is None:
            raise Exception(f"Product with id {id} does not exist")
        products.append(product)

    total = sum(p.price for p in products)
    order = Order(
        id=str(uuid.uuid4()),
        product_ids=product_ids,
        total=total,
    )
    save(order)

    return order

def order_get_by_id(id: str) -> Order:
    return get_by_id(id)

def order_get_many(page: int, limit: int) -> List[Order]:
    return get_many(page, limit)

