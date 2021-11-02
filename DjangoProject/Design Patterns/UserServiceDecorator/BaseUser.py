from abc import abstractmethod


class BaseUser:

    @abstractmethod
    def request_statistics(self, *args) -> str:
        pass

