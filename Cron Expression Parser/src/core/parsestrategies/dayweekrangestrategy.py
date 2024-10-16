from src.abstract.cronparsestrategy import CronParseStrategy
from src.core.cronfieldparserfactory import CronFieldParserFactory
from src.config.constants import FieldTypes
from src.config.constants import DayWeekFormats
from src.custom.cronexceptions import CronParsingError

# DayOfWeekRangeCronStrategy to handle day of week ranges like MON-FRI
class DayOfWeekRangeCronStrategy(CronParseStrategy):
    def parse(self, expression: str) -> dict:
        fields = expression.split()
        if len(fields) != 6:
            raise CronParsingError("Invalid cron format")

        try:
            minute = CronFieldParserFactory.get_parser(FieldTypes.MINUTE).parse(fields[0])
            hour = CronFieldParserFactory.get_parser(FieldTypes.HOUR).parse(fields[1])
            day_of_month = CronFieldParserFactory.get_parser(FieldTypes.DAYOFMONTH).parse(fields[2])
            month = CronFieldParserFactory.get_parser(FieldTypes.MONTH).parse(fields[3])
            day_of_week = CronFieldParserFactory.get_parser(FieldTypes.DAYOFWEEK).parse(fields[4], DayWeekFormats.MONTOFRIDAY)
            command = fields[5]
        except Exception as e:
            raise CronParsingError(e)

        return {
            FieldTypes.MINUTE.value: minute,
            FieldTypes.HOUR.value: hour,
            FieldTypes.DAYOFMONTH.value: day_of_month,
            FieldTypes.MONTH.value: month,
            FieldTypes.DAYOFWEEK.value: day_of_week,
            FieldTypes.COMMAND.value: command
        }
