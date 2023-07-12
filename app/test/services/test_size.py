from unittest.mock import patch
import pytest
from app.controllers.size import SizeController
from app.test.utils.functions import get_random_string, get_random_price

def test_get_sizes_service_returns_sizes__when_sizes_found(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)


def test_get_sizes_returns_error_when_bad_request(client,size_uri):
    with patch.object(SizeController, 'get_all', return_value=(None, "Error retrieving sizes")):
        response = client.get(size_uri)
    pytest.assume(response.status.startswith('400'))
    expected_response = {'error': "Error retrieving sizes"}
    expected_status_code = 400
    assert response.status_code == expected_status_code
    assert response.json == expected_response
    
 
def test_update_size_service(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size, 'name': get_random_string(), 'price': get_random_price(1, 5)}
    response = client.put(size_uri, json=update_data)
    pytest.assume(response.status.startswith('200'))
    updated_size = response.json
    for param, value in update_data.items():
        pytest.assume(updated_size[param] == value)


def test_get_size_by_id_service(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}id/{current_size["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_size = response.json
    for param, value in current_size.items():
        pytest.assume(returned_size[param] == value)


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        pytest.assume(size['_id'] in returned_sizes)
