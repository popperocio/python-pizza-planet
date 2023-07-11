from unittest.mock import patch
import pytest
from app.controllers.size import SizeController

def test_get_sizes_service_returns_sizes__when_sizes_found(client, create_sizes, size_uri):
    response = client.get(size_uri)
    pytest.assume(response.status.startswith('200'))


def test_get_sizes_returns_error_when_bad_request(client,size_uri):
    with patch.object(SizeController, 'get_all', return_value=(None, "Error retrieving sizes")):
        response = client.get(size_uri)
    pytest.assume(response.status.startswith('400'))
    
 