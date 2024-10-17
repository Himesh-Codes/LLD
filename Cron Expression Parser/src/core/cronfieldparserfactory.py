# Factory for creating specific field parsers
from src.abstract.cronfieldparser import CronFieldParser
from src.core.fieldparsers.dayofmonthfield import DayOfMonthFieldParser
from src.core.fieldparsers.minutefield import MinuteFieldParser
from src.core.fieldparsers.hourfield import HourFieldParser
from src.core.fieldparsers.monthfield import MonthFieldParser
from src.core.fieldparsers.dayofweekfield import DayOfWeekFieldParser
from src.core.fieldparsers.yearfield import YearFieldParser
from src.config.constants import FieldTypes
from src.custom.cronexceptions import CronParsingError

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
        elif field_type == FieldTypes.YEAR:
            return YearFieldParser()
        else:
            raise CronParsingError(f"Unsupported field type: {field_type}")