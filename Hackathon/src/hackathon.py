"""
Implementation of user class
User will solve a problem and add it into track
Get total scored which help us to find leader
Assumptions
--------------
Single hackathon is considered.
Assume the APIs and platform will be available to user on 2 days of hackathon dates. 
After that we can remove public access of APIs, this is the assumption.
Alternative: Add availbility filter in APIs main class "HackathonPlatform" for the predefined dates in a 
config.
"""

from typing import Dict, List, Optional, Tuple

from abstract.hackathon_abstract import HackathonAbstract
from config.difficulty import ProblemDifficulty
from user import User
from problem import Problem


class HackathonPlatform(HackathonAbstract):
    def __init__(self):
        self.problems: Dict[int, Problem] = {}
        self.users: Dict[int, User] = {}
        self.problem_counter = 0
        self.user_counter = 0
    
    def add_problem(self, description: str, tag: str, difficulty: ProblemDifficulty, score: int) -> int:
        self.problem_counter += 1
        problem = Problem(description, tag, difficulty, score)
        self.problems[self.problem_counter] = problem
        return self.problem_counter
    
    def add_user(self, name: str, department: str) -> int:
        self.user_counter += 1
        user = User(name, department)
        self.users[self.user_counter] = user
        return self.user_counter
    
    def fetch_problems(self, difficulty: Optional[ProblemDifficulty] = None, tag: Optional[str] = None, sort_by: Optional[str] = None) -> List[Problem]:
        problems = list(self.problems.values())
        
        if difficulty:
            problems = [p for p in problems if p.difficulty == difficulty]
        
        if tag:
            problems = [p for p in problems if p.tag == tag]
        
        if sort_by == 'score':
            problems.sort(key=lambda x: x.score, reverse=True)
        
        return problems
    
    def solve_problem(self, user_id: int, problem_id: int, time_taken: float):
        try:
            user = self.users[user_id]
            problem = self.problems[problem_id]
        except KeyError:
            print("Invalid user or problem ID")
            return
        
        try:
            user.solve_problem(problem_id, problem.score, time_taken)
            problem.add_solution(user_id, time_taken)
        except ValueError as e:
            print(f"Error: {e}")
    
    def fetch_solved_problems(self, user_id: int) -> List[Tuple[int, int, float]]:
        try:
            user = self.users[user_id]
        except KeyError:
            print("Invalid user ID")
            return
        
        return [(problem_id, score, time_taken) for problem_id, (score, time_taken) in user.solved_problems.items()]
    
    # Leader selection based on problem solved score attained
    def get_leader(self) -> Tuple[str, str]:
        max_score = -1
        leader = None
        
        for user in self.users.values():
            total_score = user.get_total_score()
            if total_score > max_score:
                max_score = total_score
                leader = user
        
        if not leader:
            print("No leader found")
            return
        
        return leader.name, leader.department
    
    # Get stat of a problem
    def problem_stats(self, problem_id: int) -> Tuple[int, float]:
        try:
            problem = self.problems[problem_id]
        except KeyError:
            print("Invalid problem ID")
            return
        
        return problem.get_stats()
