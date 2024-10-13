from abstract.cronparsestrategy import CronParseStrategy
from core.cronfieldparserfactory import CronFieldParserFactory


# DayOfWeekRangeCronStrategy to handle day of week ranges like MON-FRI
class DayOfWeekRangeCronStrategy(CronParseStrategy):
    def parse(self, expression: str) -> dict:
        fields = expression.split()
        if len(fields) != 6:
            raise ValueError("Invalid cron format")

        minute = CronFieldParserFactory.get_parser("minute").parse(fields[0])
        hour = CronFieldParserFactory.get_parser("hour").parse(fields[1])
        day_of_month = CronFieldParserFactory.get_parser("day of month").parse(fields[2])
        month = CronFieldParserFactory.get_parser("month").parse(fields[3])
        day_of_week = CronFieldParserFactory.get_parser("day of week").parse(fields[4])
        command = fields[5]

        return {
            "minute": minute,
            "hour": hour,
            "day of month": day_of_month,
            "month": month,
            "day of week": day_of_week,
            "command": command
        }
