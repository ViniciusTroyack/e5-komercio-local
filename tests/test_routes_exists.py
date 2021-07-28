from pytest import fail
from werkzeug.exceptions import NotFound
from werkzeug.exceptions import InternalServerError


def test_route_list_exists(route_matcher):
    try:
        assert route_matcher("/products")
    except NotFound:
        fail('Verifique se a rota "/products" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/products", essa rota não é capaz de processar uma requisição'
        )


def test_route_obtain_specific_product(route_matcher):
    try:
        assert route_matcher("/products/1")
    except NotFound:
        fail('Verifique se a rota "/products/<product_id>" existe')
    except InternalServerError:
        fail(
            'Seu servidor está com erro interno na rota "/products", essa rota não é capaz de processar uma requisição'
        )
