import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.abstract.cronparsestrategy import CronParseStrategy
from src.core.cronfieldparserfactory import CronFieldParserFactory
from src.config.constants import FieldTypes
from src.custom.cronexceptions import CronParsingError

# Year Cron strategy
class YearCronStrategy(CronParseStrategy):
    def parse(self, expression: str) -> dict:
        fields = expression.split()
        if len(fields) != 7:
            raise CronParsingError("Invalid cron format")
        
        try:
            minute = CronFieldParserFactory.get_parser(FieldTypes.MINUTE).parse(fields[0])
            hour = CronFieldParserFactory.get_parser(FieldTypes.HOUR).parse(fields[1])
            day_of_month = CronFieldParserFactory.get_parser(FieldTypes.DAYOFMONTH).parse(fields[2])
            month = CronFieldParserFactory.get_parser(FieldTypes.MONTH).parse(fields[3])
            day_of_week = CronFieldParserFactory.get_parser(FieldTypes.DAYOFWEEK).parse(fields[4])
            year = CronFieldParserFactory.get_parser(FieldTypes.YEAR).parse(fields[5])
            command = fields[6]
        except Exception as e:
            raise CronParsingError(e)

        return {
            FieldTypes.MINUTE.value: minute,
            FieldTypes.HOUR.value: hour,
            FieldTypes.DAYOFMONTH.value: day_of_month,
            FieldTypes.MONTH.value: month,
            FieldTypes.DAYOFWEEK.value: day_of_week,
            FieldTypes.YEAR.value: year,
            FieldTypes.COMMAND.value: command
        }