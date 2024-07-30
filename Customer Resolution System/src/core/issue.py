from typing import List, Dict, Optional, Any

from config.issue_type import IssueType
from config.status import IssueStatus

class Issue:
    def __init__(self, issue_id: str, transaction_id: str, issue_type: IssueType, subject: str, description: str, email: str):
        self.issue_id = issue_id
        self.transaction_id = transaction_id
        self.issue_type = issue_type
        self.subject = subject
        self.description = description
        self.email = email
        self.status = IssueStatus.OPEN

