from abstract.cronparsestrategy import CronParseStrategy
from core.cronfieldparserfactory import CronFieldParserFactory
from config.constants import FieldTypes
from config.constants import DayWeekFormats
from custom.cronexceptions import CronParsingError

# Standard Cron strategy
class StandardCronStrategy(CronParseStrategy):
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
            FieldTypes.MINUTE: minute,
            FieldTypes.HOUR: hour,
            FieldTypes.DAYOFMONTH: day_of_month,
            FieldTypes.MONTH: month,
            FieldTypes.DAYOFWEEK: day_of_week,
            FieldTypes.COMMAND: command
        }