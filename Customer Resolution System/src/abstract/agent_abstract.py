from abc import ABC, abstractmethod
from typing import Dict, List, Optional

from config.issue_type import IssueType
from core.agent import Agent

class AgentAbstract(ABC):
    @abstractmethod
    def add_agent(self, agent_id: str, name: str, expertise: List[IssueType]) -> Agent:
        raise NotImplementedError
    
    @abstractmethod
    def assign_issue(self, issue_id: str) -> Optional[Agent]:
        raise NotImplementedError
    
    @abstractmethod
    def view_agents_work_history(self) -> Dict[str, List[str]]:
        raise NotImplementedError
    
    @abstractmethod
    def get_agent(self, agent_id: str) -> Optional[Agent]:
        raise NotImplementedError