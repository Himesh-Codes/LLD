import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import threading
from src.custom.singleton import singleton
from src.cronparser import CronParser
from src.custom.cronexceptions import CronParsingError
from src.config.parsestrategy import ParseStrategy

# CronApp Class to handle multiple cron expressions with multithreading
@singleton
class CronApp:
    def __init__(self):
        self.lock = threading.Lock()  # Lock for synchronization

    def run(self, cron_expression: str = None, cronformat = None, cron_expressions: dict = None):
        if cron_expressions:
            threads = []
            for expr, format in cron_expressions.items():
                thread = threading.Thread(target=self.parse_and_print, args=(expr,format))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
        elif cron_expression and cronformat:
            self.parse_and_print(cron_expression, cronformat)

    def parse_and_print(self, expr: str, strategy):
        cron_parser = CronParser(expr, strategy)
        parsed = cron_parser.parse()

        # Ensure the output is synchronized across threads
        with self.lock:
            try:
                for field, values in parsed.items():
                    if isinstance(values, list):
                        # filling with space '<' alignment specifier
                        print(f"{field:<14} {' '.join(map(str, values))}")
                    else:
                        print(f"{field:<14} {values}")
            except Exception as e:
                raise CronParsingError(e)

