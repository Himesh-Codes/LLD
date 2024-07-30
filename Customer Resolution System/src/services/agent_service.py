from typing import Dict, List, Optional
from abstract.agent_abstract import AgentAbstract
from abstract.assignment_abstract import AgentAssignmentStrategy
from config.issue_type import IssueType
from core.agent import Agent
from core.exceptions import IssueNotFoundException
from issue_service import IssueService
from assignment_service import AssignmentService


class AgentService(AgentAbstract):
    def __init__(self, strategy: AgentAssignmentStrategy, issue_service: IssueService):
        self.agents: Dict[str, Agent] = {}
        self.issue_service = issue_service
        self.assignment_service = AssignmentService(strategy, list(self.agents.values()))

    def add_agent(self, agent_id: str, name: str, expertise: List[IssueType]) -> Agent:
        if agent_id in self.agents:
            raise ValueError(f"Agent with ID {agent_id} already exists")
        agent = Agent(agent_id, name, expertise)
        self.agents[agent_id] = agent
        # Update the assignment service with new agents
        self.assignment_service.agents = list(self.agents.values())
        return agent

    def assign_issue(self, issue_id: str) -> Optional[Agent]:
        try:
            issue = self.issue_service.issues.get(issue_id)
        except ValueError:
            raise IssueNotFoundException(f"Issue with ID {issue_id} not found")
        
        selected_agent = self.assignment_service.assign_issue(issue)
        return selected_agent

    def view_agents_work_history(self) -> Dict[str, List[str]]:
        work_history = {agent_id: [] for agent_id in self.agents}
        for issue_id, completed_issue in self.issue_service.completed_issues.items():
            work_history[completed_issue.agent_id].append(issue_id)
        return work_history

    def get_agent(self, agent_id: str) -> Optional[Agent]:
        return self.agents.get(agent_id)
