from ..repositories.managers import ReportManager
from .base import BaseController
from sqlalchemy.exc import SQLAlchemyError

class ReportController(BaseController):
    manager = ReportManager


    @classmethod
    def get_reports(cls):
        try:
            return ReportManager.get_reports(), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)