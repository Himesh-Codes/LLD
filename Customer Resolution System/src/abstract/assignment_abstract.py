from abc import ABC, abstractmethod
from typing import List

from core.agent import Agent
from core.issue import Issue


class AgentAssignmentStrategy(ABC):
    
    @abstractmethod
    def assign(self, issue: Issue, agents: List[Agent]) -> Agent:
        """
        Assign the given issue to one of the available agents based on the strategy.
        :param issue: The issue to be assigned.
        :param agents: List of available agents.
        :return: The selected agent.
        """
        pass
