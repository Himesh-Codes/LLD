from abc import ABC, abstractmethod
from config.difficulty import ProblemDifficulty
from problem import Problem
from typing import List, Optional, Tuple
class HackathonAbstract(ABC):
    @abstractmethod
    def add_problem(self, description: str, tag: str, difficulty: ProblemDifficulty, score: int) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def add_user(self, name: str, department: str) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def fetch_problems(self, difficulty: Optional[ProblemDifficulty] = None, tag: Optional[str] = None, sort_by: Optional[str] = None) -> List[Problem]:
        raise NotImplementedError
    
    @abstractmethod
    def solve_problem(self, user_id: int, problem_id: int, time_taken: float):
        raise NotImplementedError
    
    @abstractmethod
    def fetch_solved_problems(self, user_id: int) -> List[Tuple[int, int, float]]:
        raise NotImplementedError
    
    @abstractmethod
    def get_leader(self) -> Tuple[str, str]:
        raise NotImplementedError
    
    @abstractmethod
    def problem_stats(self, problem_id: int) -> Tuple[int, float]:
        raise NotImplementedError
    
    

