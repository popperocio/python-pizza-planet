from abc import ABC, abstractmethod

from .concrete_creator_report import ConcreteReport


class ReporterFactory():
        
        
    def __init__(self,report):
        self.report = report


    def factory_method(self):
        if self.report== "report":
            report = ConcreteReport().create_report()
            return report

    
