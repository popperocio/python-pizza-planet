from unittest.mock import patch
import pytest
from app.controllers.size import SizeController

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
    
 