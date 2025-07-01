from marshmallow import Schema, fields

class OrderCreaeHttpBodySchema(Schema):
    product_ids = fields.List(fields.String())

class OrderGetParamsSchema(Schema):
    page = fields.Int()
    limit = fields.Int()