from statistics import mean
from typing import List
from Strategy import Strategy


class MeanStrategy(Strategy):
    def compute_value(self, computation_values: List) -> List:
        return mean(computation_values)
