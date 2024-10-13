# Custom Exceptions
class CronParsingError(Exception):
    """Custom exception for errors in parsing the cron expression."""
    pass

class FieldExpansionError(Exception):
    """Custom exception for errors in expanding fields in the cron expression."""
    pass