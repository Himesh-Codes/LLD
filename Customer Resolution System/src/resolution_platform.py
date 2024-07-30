
from typing import List, Dict, Optional

from abstract.assignment_abstract import AgentAssignmentStrategy
from core.agent import Agent
from core.issue import Issue
from services.agent_service import AgentService
from services.assignment_service import AssignmentService
from services.issue_service import IssueService

class ResolutionPlatform:
    def __init__(self, strategy: AgentAssignmentStrategy):
        self.issue_service = IssueService()
        self.agent_service = AgentService(strategy, self.issue_service)
        self.assignment_service = AssignmentService(strategy, list(self.agent_service.agents.values()))

    # Issue Service APIs
    def create_issue(self, transaction_id: str, issue_type: str, subject: str, description: str, email: str) -> Issue:
        return self.issue_service.create_issue(transaction_id, issue_type, subject, description, email)

    def get_issues(self, filter_criteria: Dict[str, str]) -> List[Issue]:
        return self.issue_service.get_issues(filter_criteria)

    def update_issue(self, issue_id: str, status: str, resolution: Optional[str] = None) -> Issue:
        return self.issue_service.update_issue(issue_id, status, resolution)

    def resolve_issue(self, issue_id: str, agent_id: str, resolution: str) -> Issue:
        agent = self.agent_service.get_agent(agent_id)
        if not agent:
            raise ValueError(f"Agent with ID {agent_id} not found")
        return self.issue_service.resolve_issue(issue_id, resolution, agent_id)

    # Agent Service APIs
    def add_agent(self, agent_id: str, name: str, expertise: List[str]) -> Agent:
        return self.agent_service.add_agent(agent_id, name, expertise)

    def assign_issue(self, issue_id: str) -> Optional[Agent]:
        issue = self.issue_service.issues.get(issue_id)
        if not issue:
            raise ValueError(f"Issue with ID {issue_id} not found")
        return self.agent_service.assign_issue(issue_id)

    def view_agents_work_history(self) -> Dict[str, List[str]]:
        return self.agent_service.view_agents_work_history()

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        return self.agent_service.get_agent(agent_id)
