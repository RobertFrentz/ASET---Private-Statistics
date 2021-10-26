from abc import abstractmethod
class Strategy:

    @abstractmethod
    def protocol_algorithm(self):
        pass

    @abstractmethod
    def print_protocol_message(self):
        pass