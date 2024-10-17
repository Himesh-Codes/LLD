from enum import Enum

class ParseStrategy(Enum):
    STANDARD = "standard"
    DAYWEEKRANGE = "dayweekrange"
    ARGUMENT = "argumentformat"
    YEAR = "year"