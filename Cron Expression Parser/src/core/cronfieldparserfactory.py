# Factory for creating specific field parsers
from abstract.cronfieldparser import CronFieldParser
from core.fieldparsers.dayofmonthfield import DayOfMonthFieldParser
from core.fieldparsers.minutefield import MinuteFieldParser
from core.fieldparsers.hourfield import HourFieldParser
from core.fieldparsers.monthfield import MonthFieldParser
from core.fieldparsers.dayofweekfield import DayOfWeekFieldParser
from config.constants import FieldTypes
from custom.cronexceptions import CronParsingError

class CronFieldParserFactory:
    @staticmethod
    def get_parser(field_type: str) -> CronFieldParser:
        if field_type == FieldTypes.MINUTE:
            return MinuteFieldParser()
        elif field_type == FieldTypes.HOUR:
            return HourFieldParser()
        elif field_type == FieldTypes.DAYOFMONTH:
            return DayOfMonthFieldParser()
        elif field_type == FieldTypes.MONTH:
            return MonthFieldParser()
        elif field_type == FieldTypes.DAYOFWEEK:
            return DayOfWeekFieldParser()
        else:
            raise CronParsingError(f"Unsupported field type: {field_type}")