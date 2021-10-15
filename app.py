from products import lista_de_produtos
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/products')
def list_products():

    page = request.args.get('page')
    per_page = request.args.get('per_page')

    if page:
        if per_page:
            return jsonify(lista_de_produtos[:int(per_page)])

    return jsonify(lista_de_produtos)

@app.get('/products/<product_id>')
def get_product(product_id):

    output = [product for product in lista_de_produtos if product['id'] == int(product_id)]
    
    if len(output) == 0:
        return jsonify('produto não encontrado'), 404

    return jsonify(output)
