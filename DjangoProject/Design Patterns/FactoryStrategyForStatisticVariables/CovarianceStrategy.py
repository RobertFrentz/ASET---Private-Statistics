from typing import List
import numpy as np

from Strategy import Strategy


class CovarianceStrategy(Strategy):
    def compute_value(self, computation_values: List) -> np.ndarray:
        return np.cov(computation_values)
