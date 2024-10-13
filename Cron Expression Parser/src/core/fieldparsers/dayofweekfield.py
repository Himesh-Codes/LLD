# Concrete Classes for Field Parser
from abstract.cronfieldparser import CronFieldParser
from core.cronfield import CronField

class DayOfWeekFieldParser(CronFieldParser):
    day_map = {'MON': 1, 'TUE': 2, 'WED': 3, 'THU': 4, 'FRI': 5, 'SAT': 6, 'SUN': 0}

    def parse(self, field_expr: str):
        if any(day in field_expr.upper() for day in self.day_map):
            return self._expand_day_of_week_range(field_expr)
        else:
            return CronField(field_expr, 0, 6).expand()

    def _expand_day_of_week_range(self, day_field):
        """
        Expands day-of-week field, handling ranges like MON-FRI or individual days like MON.
        """
        if "-" in day_field:
            start_day, end_day = day_field.split("-")
            start = self.day_map[start_day.upper()]
            end = self.day_map[end_day.upper()]
            return list(range(start, end + 1))
        elif "," in day_field:
            days = day_field.split(",")
            return sorted(set(self.day_map[day.upper()] for day in days))
        else:
            return [self.day_map[day_field.upper()]]