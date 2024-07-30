from typing import Dict, List, Optional
from abstract.issue_abstract import IssueAbstract
from config.filter_type import FilterType
from config.issue_type import IssueType
from config.status import IssueStatus
from core.exceptions import GeneralException, IssueNotFoundException, ValueException
from core.issue import Issue
from core.issue_completions import IssueResolutionHistory
from utility.issue_id_generator import IssueIdGenerator


class IssueService(IssueAbstract):

    def __init__(self):
            self.issues: Dict[str, Issue] = {}
            self.id_generator = IssueIdGenerator()
            self.completed_issues: Dict[str, IssueResolutionHistory] = {}

    def create_issue(self, transaction_id: str, issue_type: str, subject: str, description: str, email: str) -> Issue:
        try:
            issue_id = self.id_generator.generate_id()
        except ValueError:
            raise ValueException(f"No issue id value generated")
        
        new_issue = Issue(issue_id, transaction_id, issue_type, subject, description, email)
        self.issues[issue_id] = new_issue
        return new_issue

    def get_issues(self, filter_by: Optional[Dict[FilterType, IssueType]] = None) -> List[Issue]:
        if not filter_by:
            return list(self.issues.values())

        filtered_issues = []
        for issue in self.issues.values():
            match = True
            for key, value in filter_by.items():
                if getattr(issue, key) != value:
                    match = False
                    break
            if match:
                filtered_issues.append(issue)
        return filtered_issues

    def update_issue(self, issue_id: str, status: Optional[IssueStatus] = None) -> Issue:
        try:
            issue = self.issues.get(issue_id)
        except KeyError:
                raise IssueNotFoundException(f"Issue with ID {issue_id} not found")
        if status:
            issue.status = status
        return issue

    def resolve_issue(self, issue_id: str, agent_id: str, resolution: str) -> IssueResolutionHistory:
        self.update_issue(issue_id, status=IssueStatus.RESOLVED)
        try:
            completed_issue = IssueResolutionHistory(issue_id, agent_id, resolution)
            self.completed_issues[issue_id] = completed_issue
            del self.issues[issue_id]
        except RuntimeError:
            raise GeneralException(f"Problem in resolving issue")
        return completed_issue
