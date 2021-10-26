from abc import abstractmethod
from typing import List


class Strategy:

    @abstractmethod
    def compute_value(self, computation_values: List):
        pass
