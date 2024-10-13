# Concrete Classes for Field Parser
from src.abstract.cronfieldparser import CronFieldParser
from src.core.cronfield import CronField
from src.config.constants import DayWeekFormats
from src.config.constants import DAY_MAP
from src.custom.cronexceptions import FieldExpansionError

class DayOfWeekFieldParser(CronFieldParser):

    def parse(self, field_expr: str, format: DayWeekFormats = DayWeekFormats.INTEGERDAYS):
        if format == DayWeekFormats.MONTOFRIDAY:
            return self._expand_day_of_week_range(field_expr)
        else:
            return CronField(field_expr, 0, 6).expand()

    def _expand_day_of_week_range(self, day_field):
        """
        Expands day-of-week field, handling ranges like MON-FRI or individual days like MON.
        """
        try:
            if "-" in day_field:
                start_day, end_day = day_field.split("-")
                start = DAY_MAP[start_day.upper()]
                end = DAY_MAP[end_day.upper()]
                if not(0 <= start <= 6 and 0 <= end <= 6 and start < end):
                    raise FieldExpansionError(f"Invalid range for week days") 
                return list(range(start, end + 1))
            elif "," in day_field:
                days = day_field.split(",")
                return sorted(set(DAY_MAP[day.upper()] for day in days))
            else:
                return [DAY_MAP[day_field.upper()]]
        except Exception as e:
            raise FieldExpansionError(e)