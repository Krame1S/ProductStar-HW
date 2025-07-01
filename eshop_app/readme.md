# Домашнее задание по REST API Flask E-Shop app

## How to Run the Server

1. Create a virtual environment: `python3 -m venv .venv`
2. Activate the virtual environment: `source .venv/bin/activate`
3. Install dependencies: `pip install flask marshmallow`
4. Run the server: `python3 server.py`

## How to Create a Product

POST request example:

```bash
curl localhost:5000/api/v1/product -X POST -H 'Content-Type: application/json' -d '{"name": "Phone", "price": 20.0}'
```

Response:

```json
{
  "id": "your generated uuid",
  "name": "Phone",
  "price": 20.0
}
```

## How to Get All Products

Send a GET request to `/api/v1/product` with query parameters `page` and `limit`.

Example:

```bash
curl "localhost:5000/api/v1/product?page=0&limit=10"
```

Response:

```json
[
  {
    "id": "1",
    "name": "Телевизор",
    "price": 15.0
  },
  {
    "id": "2",
    "name": "Кофемашина",
    "price": 10.0
  }
]
```

## How to Get a Product by ID

Send a GET request to `/api/v1/product/<id>` with the product ID.

Example:

```bash
curl localhost:5000/api/v1/product/1
```

Response:

```json
{
  "id": "1",
  "name": "Телевизор",
  "price": 15.0
}
```

If the product is not found:

```json
{
  "error": "Not found"
}
```
