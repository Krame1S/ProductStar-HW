from flask import Flask, request
from marshmallow import ValidationError

from app.logic.order_logic import order_create, order_get_by_id, order_get_many
from app.logic.product_logic import product_create, product_get_by_id, product_get_many
from app.view.order_schemas import OrderCreateDtoSchema, OrderSchema, OrderGetManyParams
from app.view.product_schemas import ProductCreateDtoSchema, ProductGetManyParams, ProductSchema

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)

@app.post("/api/v1/product")
def product_create_endpoint():
    try:
        product_create_dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        product = product_create(
            name=product_create_dto['name'],
            price=product_create_dto['price']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return ProductSchema().dump(product)

@app.get("/api/v1/product")
def product_get_many_endpoint():
    try:
        product_get_many_params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    products = product_get_many(
        page=product_get_many_params['page'],
        limit=product_get_many_params['limit'],
    )

    return ProductSchema(many=True).dump(products)

@app.get("/api/v1/product/<id>")
def product_get_by_id_endpoint(id):
    product = product_get_by_id(id)

    if product is None:
        return {
            "error": 'Not found'
        }, 404

    return ProductSchema().dump(product)

def run_server():
    app.run()