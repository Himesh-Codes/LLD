from typing import List
from abstract.assignment_abstract import AgentAssignmentStrategy
from agent_service import Agent
from issue_service import Issue

class AssignmentService:
    def __init__(self, strategy: AgentAssignmentStrategy, agents: List[Agent]):
        self.strategy = strategy
        self.agents = agents

    def assign_issue(self, issue: Issue) -> Agent:
        eligible_agents = [agent for agent in self.agents if issue.issue_type in agent.expertise]
        if not eligible_agents:
            raise ValueError(f"No agents available to handle issue of type {issue.issue_type}")
        selected_agent = self.strategy.assign(issue, eligible_agents)
        selected_agent.current_workload += 1
        return selected_agent
