from abc import ABC, abstractmethod

from .report import Report


class ReporterFactory():
        
        
    def __init__(self,report):
        self.report = report


    def factory_method(self):
        if self.report== "report":
            report = Report().create_report()
            return report

    
