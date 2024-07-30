from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from config.filter_type import FilterType
from config.issue_type import IssueType
from config.status import IssueStatus
from core.issue import Issue
from core.issue_completions import IssueResolutionHistory

class IssueAbstract(ABC):
    @abstractmethod
    def create_issue(self, transaction_id: str, issue_type: str, subject: str, description: str, email: str) -> Issue:
        raise NotImplementedError
    
    @abstractmethod
    def get_issues(self, filter_by: Optional[Dict[FilterType, IssueType]] = None) -> List[Issue]:
        raise NotImplementedError
    
    @abstractmethod
    def update_issue(self, issue_id: str, status: Optional[IssueStatus] = None) -> Issue:
        raise NotImplementedError
    
    @abstractmethod
    def resolve_issue(self, issue_id: str, agent_id: str, resolution: str) -> IssueResolutionHistory:
        raise NotImplementedError