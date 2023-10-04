from flask import Flask, jsonify, request
import json
# import sys
# print(sys.path)
# sys.path.append('/Users/danishkarur/opt/anaconda3/lib/python3.9/site-packages')
from flask_cors import CORS


app = Flask('Movie Product Server')
CORS(app)

products = [
    {'id':101, 'name': 'Roja', 'price':2.5},
    {'id':102, 'name': 'Yuva', 'price':3.0},
    {'id':103, 'name': 'Bombay', 'price':2.8}

]

# Retrieve all the products - GET Request Method
# Retrieve a product by its id - GET Request Method
# Add a product - POST Request Method
# Update a product by its id - PUT Request Method
# Delete a product by its id - DELETE Request Method

# here add all the REST API end-points here
# Example request - http://localhost:5000/products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Example request - http://localhost:5000/products/144 - with method GET
@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    return jsonify(product)

# Example request - http://localhost:5000/products - with method POST
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201

# <link rel="shortcut icon" href="https://cognitiveclass.ai/rails/active_storage/blobs/proxy/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBZ2tCIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--522cc84fcb8545e2c7581fdff46186ff5dafc1af/euve8uv2tlme8rk0h89rwkguwsph.png" type="image/x-icon" data-react-helmet="true">
# Example request - http://localhost:5000/products/144 - with method PUT
@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    id = int(id)
    updated_product = json.loads(request.data)
    product = [x for x in products if x["id"] == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return '', 204

# Example request - http://localhost:5000/products/144 - with method DELETE
@app.route('/products/<id>', methods=['DELETE'])
def remove_product(id):
    id = int(id)
    product = [x for x in products if x["id"] == id][0]
    products.remove(product)
    return '', 204
#
if __name__ == '__main__':
    app.run()
# app.run(port=5000,debug = True)
# from waitress import serve
# serve(app, host="0.0.0.0", port=8080)