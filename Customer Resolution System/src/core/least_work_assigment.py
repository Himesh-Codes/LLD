from typing import List
from abstract.assignment_abstract import AgentAssignmentStrategy
from core.agent import Agent
from core.exceptions import NoAvailableAgentException
from core.issue import Issue


class LeastWorkloadStrategy(AgentAssignmentStrategy):

    def assign(self, issue: Issue, agents: List[Agent]) -> Agent:
        eligible_agents = [agent for agent in agents if issue.issue_type in agent.expertise]
        if not eligible_agents:
            raise NoAvailableAgentException(f"No agents available to handle issue of type {issue.issue_type}")
        # Sort agents by workload to assign to the least busy agent, sorted in ascending order
        eligible_agents.sort(key=lambda agent: agent.current_workload)
        return eligible_agents[0]
