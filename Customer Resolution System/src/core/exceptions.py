# Defining exception classes we can handle multiple exceptions with different logic or loggings

class IssueNotFoundException(Exception):
    def __init__(self, e):
        print(e)

class InvalidIssueTypeException(Exception):
    def __init__(self, e):
        print(e)

class AgentNotFoundException(Exception):
    def __init__(self, e):
        print(e)

class NoAvailableAgentException(Exception):
    def __init__(self, e):
        print(e)

class ValueException(Exception):
    def __init__(self, e):
        print(e)

class GeneralException(Exception):
    def __init__(self, e):
        print(e)