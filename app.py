from products import lista_de_produtos
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get('/products')
def list_products():

    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    list_len = len(lista_de_produtos)

    if page:
        if per_page:
            paged_list = [lista_de_produtos[i:i+per_page] for i in range(0, list_len, per_page)]

    return jsonify(paged_list[page-1])

@app.get('/products')
def get_product(product_id):

    output = [product for product in lista_de_produtos if product['id'] == int(product_id)]
    
    if len(output) == 0:
        return jsonify('produto não encontrado'), 404

    return jsonify(output)
