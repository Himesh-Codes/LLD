# Concrete Classes for Field Parser
from abstract.cronfieldparser import CronFieldParser
from core.cronfield import CronField

class DayOfMonthFieldParser(CronFieldParser):
    def parse(self, field_expr: str):
        return CronField(field_expr, 1, 31).expand()