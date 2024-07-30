class IssueResolutionHistory:
    def __init__(self, issue_id: str, agent_id: str, resolution: str):
        self.issue_id = issue_id
        self.agent_id = agent_id
        self.resolution = resolution