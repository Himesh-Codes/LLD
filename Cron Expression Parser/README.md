# Cron Expression Parser

## Project structure

- /src : Contains source code
- central api class : /src/cronapp.py
- src/abstract: Defintion of abstract classes
- src/config: Config enums and app constants.
- src/custom: Custom exceptions, decorators.
- src/core: Core entities cronfield parsing logic, parsing factory, different field parsers, parsing strategies etc..

## Sample Testing

- Copy paste below code in `/src/cronapp.py` and run the file:

```
# Sample usage
if __name__ == "__main__":
    cron_expressions = {
        "*/15 0 1,15 * 1-5 /usr/bin/find": ParseStrategy.STANDARD,
        "0 0 * * MON-FRI /usr/bin/backup": ParseStrategy.DAYWEEKRANGE,
        "5 0 * * 1 /usr/bin/cleanup": ParseStrategy.STANDARD
    }
    app = CronApp()
    app.run(None, None, cron_expressions)
    app.run("*/5 * 1-15/2 * 2-3 /usr/bin/singlecron", ParseStrategy.STANDARD)

```

## Testing
