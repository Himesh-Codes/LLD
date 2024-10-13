from abc import ABC, abstractmethod

# CronField Parser Interface
class CronFieldParser(ABC):
    @abstractmethod
    def parse(self, field_expr: str):
        pass