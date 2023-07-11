import pytest

from ..utils.functions import get_random_price, get_random_string


def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'


@pytest.fixture
def beverage():
    return beverage_mock()


@pytest.fixture
def create_beverage(client, beverage_uri) -> dict:
    response = client.post(beverage_uri, json=beverage_mock())
    return response

