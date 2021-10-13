from flask import Flask, request, jsonify
from products import lista_de_produtos

app = Flask(__name__)


@app.route("/products", methods=["GET"])
def list_products():
    page = int(request.args['page']) if request.args['page'] is not None else 0
    per_page = int(request.args['per_page']) if request.args['per_page'] is not None else 10

    start = page*per_page
    end = (page+1)*per_page

    return jsonify(lista_de_produtos[start:end]), 200



@app.route("/products/<id>", methods=["GET"])
def get_product(id):
    result = []
    for item in lista_de_produtos:
        if item['id'] == int(id):
            result.append(item)

    return jsonify(result), 200
