import pytest


def test_get_reports(client, report_uri):
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))

