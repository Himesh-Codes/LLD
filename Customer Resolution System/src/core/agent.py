from typing import List

class Agent:
    def __init__(self, agent_id: str, name: str, expertise: List[str]):
        self.agent_id = agent_id
        self.name = name
        self.expertise = expertise
        self.current_workload = 0  # Number of issues currently assigned to the agent