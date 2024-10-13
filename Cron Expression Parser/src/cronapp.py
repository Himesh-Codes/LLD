import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import threading
from config.strategy import Strategy
from custom.singleton import singleton
from cronparser import CronParser

# CronApp Class to handle multiple cron expressions with multithreading
@singleton
class CronApp:
    def __init__(self, cron_expressions: dict):
        self.cron_expressions = cron_expressions
        self.lock = threading.Lock()  # Lock for synchronization

    def run(self):
        threads = []
        for expr, format in self.cron_expressions.items():
            thread = threading.Thread(target=self.parse_and_print, args=(expr,format))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    def parse_and_print(self, expr: str, strategy):
        cron_parser = CronParser(expr, strategy)
        parsed = cron_parser.parse()

        # Ensure the output is synchronized across threads
        with self.lock:
            for field, values in parsed.items():
                if isinstance(values, list):
                    # filling with space '<' alignment specifier
                    print(f"{field:<14} {' '.join(map(str, values))}")
                else:
                    print(f"{field:<14} {values}")


# Sample usage
if __name__ == "__main__":
    cron_expressions = {
        "*/15 0 1,15 * 1-5 /usr/bin/find": Strategy.STANDARD,
        "0 0 * * MON-FRI /usr/bin/backup": Strategy.DAYWEEKRANGE,
        "5 0 * * 1 /usr/bin/cleanup": Strategy.STANDARD
    }
    app = CronApp(cron_expressions)
    app.run()
