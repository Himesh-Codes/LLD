import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.cronparser import CronParser
from src.custom.cronexceptions import CronParsingError
from src.config.parsestrategy import ParseStrategy

class TestCronFieldParser(unittest.TestCase):
    def setUp(self):
        # Prepare valid and invalid cron expressions for testing
        self.valid_expression = "*/15 0 1,15 * 1-5 /usr/bin/find"
        self.valid_argument_expression = "*/15 0 1,15 * 1-5 /usr/bin/find -v foo -v koo"
        self.valid_year_expression = "*/15 0 1,15 * 1-5 2024-2028 /usr/bin/find"
        self.invalid_minute_expression = "60 0 1,15 * 1-5 /usr/bin/find"  # Invalid minute (60)
        self.invalid_hour_expression = "*/15 25 1,15 * 1-5 /usr/bin/find"  # Invalid hour (25)
        self.invalid_day_of_month_expression = "*/15 0 32 * 1-5 /usr/bin/find"  # Invalid day of month (32)
        self.invalid_day_of_week_expression = "*/15 0 1,15 * 8 /usr/bin/find"  # Invalid day of week (8)
        self.command = "/usr/bin/find"
        self.arg_command = "/usr/bin/find -v foo -v koo"

    def test_valid_cron_expression(self):
        strategy = ParseStrategy.STANDARD
        parser = CronParser(self.valid_expression, strategy)
        result = parser.parse()

        # Validate that fields are correctly parsed
        self.assertEqual(result['minute'], [0, 15, 30, 45])
        self.assertEqual(result['hour'], [0])
        self.assertEqual(result['day of month'], [1, 15])
        self.assertEqual(result['month'], list(range(1, 13)))  # Full year
        self.assertEqual(result['day of week'], list(range(1, 6))) 
        self.assertEqual(result['command'], self.command)
    
    def test_valid__year_cron_expression(self):
        strategy = ParseStrategy.YEAR
        parser = CronParser(self.valid_year_expression, strategy)
        result = parser.parse()

        # Validate that fields are correctly parsed
        self.assertEqual(result['minute'], [0, 15, 30, 45])
        self.assertEqual(result['hour'], [0])
        self.assertEqual(result['day of month'], [1, 15])
        self.assertEqual(result['month'], list(range(1, 13)))  # Full year
        self.assertEqual(result['day of week'], list(range(1, 6))) 
        self.assertEqual(result['year'], list(range(2024, 2029))) 
        self.assertEqual(result['command'], self.command)

    def test_valid__argument_cron_expression(self):
        strategy = ParseStrategy.ARGUMENT
        parser = CronParser(self.valid_argument_expression, strategy)
        result = parser.parse()

        # Validate that fields are correctly parsed
        self.assertEqual(result['minute'], [0, 15, 30, 45])
        self.assertEqual(result['hour'], [0])
        self.assertEqual(result['day of month'], [1, 15])
        self.assertEqual(result['month'], list(range(1, 13)))  # Full year
        self.assertEqual(result['day of week'], list(range(1, 6))) 
        self.assertEqual(result['command'], self.arg_command)

    def test_invalid_minute_expression(self):
        strategy = ParseStrategy.STANDARD
        parser = CronParser(self.invalid_minute_expression, strategy)
        
        # Expect an exception due to invalid minute field
        with self.assertRaises(CronParsingError):
            parser.parse()

    def test_invalid_hour_expression(self):
        strategy = ParseStrategy.STANDARD
        parser = CronParser(self.invalid_hour_expression, strategy)
        
        # Expect an exception due to invalid hour field
        with self.assertRaises(CronParsingError):
            parser.parse()

    def test_invalid_day_of_month_expression(self):
        strategy = ParseStrategy.STANDARD
        parser = CronParser(self.invalid_day_of_month_expression, strategy)
        
        # Expect an exception due to invalid day of month field
        with self.assertRaises(CronParsingError):
            parser.parse()

    def test_invalid_day_of_week_expression(self):
        strategy = ParseStrategy.STANDARD
        parser = CronParser(self.invalid_day_of_week_expression, strategy)
        
        # Expect an exception due to invalid day of week field
        with self.assertRaises(CronParsingError):
            parser.parse()

    def test_day_of_week_range_strategy(self):
        # Test the new DayOfWeekRangeCronStrategy with "MON-FRI"
        expression = "0 0 * * MON-FRI /usr/bin/backup"
        strategy = ParseStrategy.DAYWEEKRANGE
        parser = CronParser(expression, strategy)
        result = parser.parse()

        self.assertEqual(result['minute'], [0])
        self.assertEqual(result['hour'], [0])
        self.assertEqual(result['day of month'], list(range(1, 32)))  # Full month
        self.assertEqual(result['month'], list(range(1, 13)))  # Full year
        self.assertEqual(result['day of week'], [1, 2, 3, 4, 5])  # Monday to Friday
        self.assertEqual(result['command'], "/usr/bin/backup")

    def test_day_of_week_invalid_strategy(self):
        # Test DayOfWeekRangeCronStrategy with invalid days (e.g., "SAT-MON")
        invalid_expression = "0 0 * * SAT-MON /usr/bin/backup"
        strategy = ParseStrategy.DAYWEEKRANGE
        parser = CronParser(invalid_expression, strategy)

        # Expect an exception due to invalid day of week range
        with self.assertRaises(CronParsingError):
            parser.parse()

if __name__ == '__main__':
    unittest.main()
