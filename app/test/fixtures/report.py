import pytest

from ..utils.functions import (get_random_sequence,
                               get_random_string)


def client_data_mock() -> dict:
    return {
        'client_address': get_random_string(),
        'client_dni': get_random_sequence(),
        'client_name': get_random_string(),
        'client_phone': get_random_sequence()
    }


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def get_reports_fixture():
    report = {}
    best_customers = [
        {"client_name": "Customer 1", "total_sales": 100},
        {"client_name": "Customer 2", "total_sales": 200}]
    most_requested_ingredient = [
            {"name": "Ingredient 1", "total_requests": 10},
            {"name": "Ingredient 2", "total_requests": 5}]
    date_with_most_revenue = [
            {"month": "January", "total_sales_revenue": 5000},
            {"month": "February", "total_sales_revenue": 8000}]
    
    report['best_customers'] = best_customers
    report['most_requested_ingredient'] = most_requested_ingredient
    report['date_with_most_revenue'] = date_with_most_revenue
    return report

@pytest.fixture
def empty_report():
    return []


