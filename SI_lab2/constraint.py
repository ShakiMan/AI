from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Dict

V = TypeVar('V')  # variable type
D = TypeVar('D')  # domain type


# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]):
        self.variables = variables

    @abstractmethod
    def satisfied(self, assigment: Dict[V, D]) -> bool:
        pass

    @abstractmethod
    def get_x_y(self):
        pass