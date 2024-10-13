# Concrete Classes for Field Parsers
from abstract.cronfieldparser import CronFieldParser
from core.cronfield import CronField

class HourFieldParser(CronFieldParser):
    def parse(self, field_expr: str):
        return CronField(field_expr, 0, 23).expand()