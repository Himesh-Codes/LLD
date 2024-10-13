from config.strategy import Strategy
from core.parsestrategies.dayweekrangestrategy import DayOfWeekRangeCronStrategy
from core.parsestrategies.standardstrategy import StandardCronStrategy

# CronParser Class Using Strategy Pattern
class CronParser:
    def __init__(self, cron_expr, strategy):
        self.cron_expr = cron_expr
        self.strategy = self._select_strategy(strategy)

    def _select_strategy(self, strategy):
        if strategy == Strategy.DAYWEEKRANGE:
            return DayOfWeekRangeCronStrategy()
        else:
            return StandardCronStrategy()  # Default standard cron strategy

    def parse(self):
        return self.strategy.parse(self.cron_expr)