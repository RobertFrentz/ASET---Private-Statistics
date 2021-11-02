from abc import abstractmethod


class DataFromFiles:

    def template_method(self) -> None:
        """
        The template method defines the skeleton of an algorithm.
        """
        self.get_age()
        self.get_bloodpressure()

    @abstractmethod
    def get_age(self) -> None:
        pass

    @abstractmethod
    def get_bloodpressure(self) -> None:
        pass