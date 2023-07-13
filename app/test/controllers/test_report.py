import pytest
from app.controllers import ReportController

def test_generate_report(app):
    _, error = ReportController.get_reports()
    pytest.assume( error is None)
