from OperationFactory import OperationFactory
from OperationType import OperationType


class ComputationUnit:
    @property
    def operation(self):
        return self._operation

    operation: OperationType

    def __init__(self, operation_factory: OperationFactory, operation: OperationType) -> None:
        self._operationFactory = operation_factory
        self._operation = operation

    @operation.setter
    def operation(self, operation_set_value: OperationType) -> None:
        self._operation = operation_set_value

    def compute_value(self) -> float:
        strategy = self._operationFactory.return_operation_strategy(self.operation)
        result = strategy.compute_value([1, 2, 3, 4, 5, 6, 7, 8, 9])
        return result
