# Concrete Classes for Field Parsers
from src.abstract.cronfieldparser import CronFieldParser
from src.core.cronfield import CronField
from src.config.constants import MAX_YEAR
from src.config.constants import MIN_YEAR

class YearFieldParser(CronFieldParser):
    def parse(self, field_expr: str):
        return CronField(field_expr, MIN_YEAR, MAX_YEAR).expand()