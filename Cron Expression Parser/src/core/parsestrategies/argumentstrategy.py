import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.abstract.cronparsestrategy import CronParseStrategy
from src.core.cronfieldparserfactory import CronFieldParserFactory
from src.config.constants import FieldTypes
from src.custom.cronexceptions import CronParsingError

# Argument Cron strategy
class ArgumentCronStrategy(CronParseStrategy):
    def parse(self, expression: str) -> dict:
        fields = expression.split()
        totalfields = len(fields)
        try:
            minute = CronFieldParserFactory.get_parser(FieldTypes.MINUTE).parse(fields[0])
            hour = CronFieldParserFactory.get_parser(FieldTypes.HOUR).parse(fields[1])
            day_of_month = CronFieldParserFactory.get_parser(FieldTypes.DAYOFMONTH).parse(fields[2])
            month = CronFieldParserFactory.get_parser(FieldTypes.MONTH).parse(fields[3])
            day_of_week = CronFieldParserFactory.get_parser(FieldTypes.DAYOFWEEK).parse(fields[4])
            command = ' '.join(fields[5: totalfields + 1])
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