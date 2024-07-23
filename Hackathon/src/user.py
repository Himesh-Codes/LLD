from abstract.user_abstract import UserAbstract

"""
Implementation of user class
User will solve a problem and add it into track
Get total scored which help us to find leader
Assumptions
--------------
Single user related data
"""

class User(UserAbstract):
    def __init__(self, name: str, department: str):
        self.name = name
        self.department = department
        self.solved_problems = {}  # problem_id: (score, time_taken)
    
    def solve_problem(self, problem_id: int, score: int, time_taken: float):
        if problem_id in self.solved_problems:
            print("Problem already solved by user")
            return
        self.solved_problems[problem_id] = (score, time_taken)
    
    def get_total_score(self):
        return sum(score for score, _ in self.solved_problems.values())
    
    def __repr__(self):
        return f"User(name={self.name}, department={self.department})"
