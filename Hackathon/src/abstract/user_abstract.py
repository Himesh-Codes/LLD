from abc import ABC, abstractmethod

class UserAbstract(ABC):
    @abstractmethod
    def solve_problem(self, problem_id: int, score: int, time_taken: float) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_total_score(self) -> int:
        raise NotImplementedError