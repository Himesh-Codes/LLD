from abc import ABC, abstractmethod
from typing import Tuple
class ProblemAbstract(ABC):
    @abstractmethod
    def add_solution(self, user_id: int, time_taken: float) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get_stats(self) -> Tuple[int, int]:
        raise NotImplementedError