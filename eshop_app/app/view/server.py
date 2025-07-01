from flask import Flask, request
from marshmallow import ValidationError

from logic.order_logic import order_create, order_get_by_id, order_get_many
from view.order_schemas import OrderCreaeHttpBodySchema, OrderGetParamsSchema

app = Flask(__name__)

@app.post('/api/v1/order')
def order_create_controller():
    try:
        dto = OrderCreaeHttpBodySchema(). loads(request.json)
    except ValidationError as err:
        return {
            'errors': err.messages
        }, 400

    try:
        order = order_create(dto["product_ids"])
    except Exception as err:
       return {
           "message": str(err)
       }, 400

    return order

@app.get('/api/v1/order/<id>')
def order_get_by_id_controller(id: str):
    order = order_get_by_id(id)
    if order is None: 
        return {
            "message": "Order not found"
        }, 404
    return order


@app.get('/api/v1/order')
def order_get_many_controller():
    try:
        params = OrderGetParamsSchema().load(request.args)
    except ValidationError as err:
        return {
            'errors': err.messages
        }, 400

    page = params.get('page')
    limit = params.get('limit')

    order = order_get_many(id)
    if order is None: 
        return {
            "message": "Order not found"
        }, 404
    return order



def run_server():
    app.run(port=5000)