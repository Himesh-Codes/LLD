from core.least_work_assigment import LeastWorkloadStrategy
from resolution_platform import ResolutionPlatform


def main():
    # Set up the strategy
    strategy = LeastWorkloadStrategy()  # or RandomAssignmentStrategy()
    resolution_platform = ResolutionPlatform(strategy)

    # Create issues
    print("Creating Issues:")
    issue1 = resolution_platform.create_issue("T1", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser1@test.com")
    issue2 = resolution_platform.create_issue("T2", "Mutual Fund Related", "Purchase Failed", "Unable to purchase Mutual Fund", "testUser2@test.com")
    issue3 = resolution_platform.create_issue("T3", "Payment Related", "Payment Failed", "My payment failed but money is debited", "testUser2@test.com")
    print(issue1)
    print(issue2)
    print(issue3)

    # Add agents
    print("\nAdding Agents:")
    agent1 = resolution_platform.add_agent("A1", "Agent One", ["Payment Related", "Gold Related"])
    agent2 = resolution_platform.add_agent("A2", "Agent Two", ["Mutual Fund Related"])
    print(agent1)
    print(agent2)

    # Assign issues
    print("\nAssigning Issues:")
    assigned_agent1 = resolution_platform.assign_issue(issue1.issue_id)
    assigned_agent2 = resolution_platform.assign_issue(issue2.issue_id)
    print(f"Issue {issue1.issue_id} assigned to {assigned_agent1.agent_id}")
    print(f"Issue {issue2.issue_id} assigned to {assigned_agent2.agent_id}")

    # Attempt to assign an issue when no agent is available
    try:
        assigned_agent3 = resolution_platform.assign_issue(issue3.issue_id)
        print(f"Issue {issue3.issue_id} assigned to {assigned_agent3.agent_id}")
    except ValueError as e:
        print(f"Error: {e}")

    # View agent work history
    print("\nAgent Work History:")
    work_history = resolution_platform.view_agents_work_history()
    for agent_id, issues in work_history.items():
        print(f"Agent {agent_id}: {issues}")

    # Resolve an issue
    print("\nResolving Issues:")
    resolved_issue = resolution_platform.resolve_issue(issue1.issue_id, "PaymentFailed debited amount will get reversed", "A1")
    print(f"Issue {resolved_issue.issue_id} resolved by {resolved_issue.agent_id}: {resolved_issue.resolution}")

    # View final agent work history
    print("\nFinal Agent Work History:")
    work_history = resolution_platform.view_agents_work_history()
    for agent_id, issues in work_history.items():
        print(f"Agent {agent_id}: {issues}")

if __name__ == "__main__":
    main()
