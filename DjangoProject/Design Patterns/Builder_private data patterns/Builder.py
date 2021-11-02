from __future__ import annotations
from abc import ABC, abstractmethod

from Protocol1 import Protocol1


class Builder(ABC):

    @property
    @abstractmethod
    def protocol(self) -> None:
        pass

    @abstractmethod
    def produce_part_init(self) -> None:
        pass

    @abstractmethod
    def produce_part_encryption(self) -> None:
        pass

    @abstractmethod
    def produce_part_decryption(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._protocol = Protocol1()

    @property
    def protocol(self) -> Protocol1:
        protocol = self._protocol
        self.reset()
        return protocol

    def produce_part_init(self) -> None:
        self._protocol.add("Init protocol")

    def produce_part_encryption(self) -> None:
        self._protocol.add("Encryption")

    def produce_part_decryption(self) -> None:
        self._protocol.add("Decryption")



