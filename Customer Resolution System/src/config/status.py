from enum import Enum

class IssueStatus(Enum):
    OPEN = "open"
    PENDING = "pending"
    RESOLVED = "resolved"