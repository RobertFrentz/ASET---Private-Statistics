from users.mean_strategy import MeanStrategy
from users.standard_deviation_strategy import StandardDeviationStrategy
from users.standard_error_strategy import StandardErrorStrategy
from users.statistics import Statistic
from users.variance_strategy import VarianceStrategy


class StrategyFactory:
    def get_strategy(self, statistic_type):
        if statistic_type == Statistic.Mean:
            mean_strategy = MeanStrategy()
            return mean_strategy
        elif statistic_type == Statistic.Variance:
            variance_strategy = VarianceStrategy()
            return variance_strategy
        elif statistic_type == Statistic.StandardDeviation:
            standard_deviation_strategy = StandardDeviationStrategy()
            return standard_deviation_strategy
        elif statistic_type == Statistic.StandardError:
            standard_error_strategy = StandardErrorStrategy()
            return standard_error_strategy
