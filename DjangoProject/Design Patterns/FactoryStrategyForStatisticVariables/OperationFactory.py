from CovarianceStrategy import CovarianceStrategy
from MeanStrategy import MeanStrategy
from OperationType import OperationType
from Strategy import Strategy


class OperationFactory:
    @staticmethod
    def return_operation_strategy(operation_type: OperationType) -> Strategy:
        if operation_type.name == OperationType.Mean:
            return MeanStrategy()
        elif operation_type.name == OperationType.Covariance:
            return CovarianceStrategy()
