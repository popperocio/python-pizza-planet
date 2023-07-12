from unittest.mock import patch
import pytest
from app.controllers import OrderController

def test_create_order_service(create_orders):
    created_order = create_orders[0]
    order = created_order.json
    pytest.assume(created_order.status.startswith('200'))
    pytest.assume(order['_id'])
    pytest.assume(order['client_address'])
    pytest.assume(order['client_dni'])
    pytest.assume(order['client_name'])
    pytest.assume(order['client_phone'])
    pytest.assume(order['date'])
    pytest.assume(order['detail'])
    pytest.assume(order['size'])
    pytest.assume(order['total_price'])
    

def test_get_orders_returns_error_when_bad_request(client,order_uri):
    with patch.object(OrderController, 'get_all', return_value=(None, "Error retrieving orders")):
        response = client.get(order_uri)
    pytest.assume(response.status.startswith('400'))
    expected_response = {'error': "Error retrieving orders"}
    expected_status_code = 400
    assert response.status_code == expected_status_code
    assert response.json == expected_response
    
    
def test_get_order_by_id_service(client,create_order, order_uri):
    current_order = create_order.json
    response = client.get(f'{order_uri}id/{current_order["_id"]}')
    pytest.assume(response.status.startswith('200'))
    returned_order = response.json
    for param, value in current_order.items():
        pytest.assume(returned_order[param] == value)
        
        
def test_get_order_by_id_service_returns_error_when_order_id_is_empty(client, create_order, order_uri):
    current_order = ""
    response = client.get(f'{order_uri}id/{current_order}')
    pytest.assume(response.status.startswith('404'))
    pytest.assume(response.status_code == 404)


def test_get_orders_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_orders = {order['_id']: order for order in response.json}
    for order in create_orders:
        pytest.assume(order.json['_id'] in returned_orders)


def test_get_orders_service_returns_empty_when_no_data_found(client, empty_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('404'))
    pytest.assume(response.json == empty_orders)
