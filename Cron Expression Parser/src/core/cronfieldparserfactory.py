# Factory for creating specific field parsers
from abstract.cronfieldparser import CronFieldParser
from core.fieldparsers.dayofmonthfield import DayOfMonthFieldParser
from core.fieldparsers.minutefield import MinuteFieldParser
from core.fieldparsers.hourfield import HourFieldParser
from core.fieldparsers.monthfield import MonthFieldParser
from core.fieldparsers.dayofweekfield import DayOfWeekFieldParser

class CronFieldParserFactory:
    @staticmethod
    def get_parser(field_type: str) -> CronFieldParser:
        if field_type == "minute":
            return MinuteFieldParser()
        elif field_type == "hour":
            return HourFieldParser()
        elif field_type == "day of month":
            return DayOfMonthFieldParser()
        elif field_type == "month":
            return MonthFieldParser()
        elif field_type == "day of week":
            return DayOfWeekFieldParser()
        else:
            raise ValueError(f"Unsupported field type: {field_type}")