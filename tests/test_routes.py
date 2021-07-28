from flask.testing import FlaskClient

from app import lista_de_produtos


def test_listing_products_status_code(client: FlaskClient, product):
    response = client.get("/products")
    assert (
        response.status_code == 200
    ), 'Verifique se sua rota "/products" suporta uma requisição mesmo com a lista "lista_de_produtos" vazia'

    lista_de_produtos.append(product)
    response = client.get("/products")
    assert (
        response.status_code == 200
    ), 'Verifique se sua rota "/products" suporta uma requisição quando a lista "lista_de_produtos" contém elementos'


def test_obtain_product_status_code(client: FlaskClient, product):
    lista_de_produtos.append(product)
    response = client.get("/products/1")
    assert (
        response.status_code == 200
    ), 'Verifique se sua rota "/products/<produto_id>" é capaz de receber uma requisição e trazer o produto encontrado'

    lista_de_produtos.clear()
    response = client.get("/products/1")
    assert (
        response.status_code == 404
    ), 'Verifique se sua rota "/products/<produto_id>" retorna uma resposta HTTP com erro 404 quando o produto buscado não existe'
