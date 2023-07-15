from abc import ABC, abstractmethod


class ReportCreator(ABC):
    
    @abstractmethod
    def create_report(cls):
        pass