from abc import ABC, abstractmethod

# Strategy Pattern Interface for Cron Expression Parsing
class CronParseStrategy(ABC):
    @abstractmethod
    def parse(self, cron_expr: str):
        pass