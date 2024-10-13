from enum import Enum

class FieldTypes(Enum):
    MINUTE = "minute"
    HOUR = "hour"
    DAYOFMONTH = "day of month"
    MONTH = "month"
    DAYOFWEEK = "day of week"
    COMMAND = "command"

class DayWeekFormats(Enum):
    INTEGERDAYS = "integerdays"
    MONTOFRIDAY = "mondaytofriday"

DAY_MAP = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 0}