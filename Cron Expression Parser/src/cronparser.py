from src.config.parsestrategy import ParseStrategy
from src.core.parsestrategies.dayweekrangestrategy import DayOfWeekRangeCronStrategy
from src.core.parsestrategies.standardstrategy import StandardCronStrategy
from src.core.parsestrategies.argumentstrategy import ArgumentCronStrategy
from src.core.parsestrategies.yearcontainedstrategy import YearCronStrategy

# CronParser Class Using Strategy Pattern
class CronParser:
    def __init__(self, cron_expr, strategy):
        self.cron_expr = cron_expr
        self.strategy = self._select_strategy(strategy)

    def _select_strategy(self, strategy):
        if strategy == ParseStrategy.DAYWEEKRANGE:
            return DayOfWeekRangeCronStrategy()
        elif strategy == ParseStrategy.ARGUMENT:
            return ArgumentCronStrategy()
        elif strategy == ParseStrategy.YEAR:
            return YearCronStrategy()
        else:
            return StandardCronStrategy()  # Default standard cron strategy

    def parse(self):
        return self.strategy.parse(self.cron_expr)