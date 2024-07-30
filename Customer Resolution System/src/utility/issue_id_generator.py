import time

# Generalise this for Agent / Issue ID generator
class IssueIdGenerator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(IssueIdGenerator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Prevent reinitialization
            self.counter = 1
            self.timestamp = int(time.time())
            self.initialized = True

    def generate_id(self) -> str:
        current_time = int(time.time())
        if current_time != self.timestamp:
            self.timestamp = current_time
            self.counter = 1
        issue_id = f"I{self.timestamp}{self.counter}"
        self.counter += 1
        return issue_id