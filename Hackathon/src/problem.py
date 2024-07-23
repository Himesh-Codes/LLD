from config.difficulty import ProblemDifficulty
from abstract.problem_abstract import ProblemAbstract

"""
Implementation of problem class
Solution entered users track
Get stat of current problem stated as problem extension
Difficulty Enum added
Assumptions
--------------
Hackathon organisers add multiple questions
"""

class Problem(ProblemAbstract):
    def __init__(self, description: str, tag: str, difficulty: ProblemDifficulty, score: int):
        self.description = description
        self.tag = tag
        self.difficulty = difficulty
        self.score = score
        self.solved_by = []  # List of (user_id, time_taken)
    
    def add_solution(self, user_id: int, time_taken: float):
        self.solved_by.append((user_id, time_taken))
    
    def __repr__(self):
        return f"Problem(description={self.description}, tag={self.tag}, difficulty={self.difficulty}, score={self.score})"
    
    def get_stats(self):
        num_solvers = len(self.solved_by)
        total_time = sum(time_taken for _, time_taken in self.solved_by)
        average_time = total_time / num_solvers if num_solvers else 0.0
        return num_solvers, average_time
