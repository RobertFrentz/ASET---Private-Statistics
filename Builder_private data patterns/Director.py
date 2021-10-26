from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from Builder import Builder


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_protocol(self) -> None:
        self.builder.produce_part_init()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_init()
        self.builder.produce_part_encryption()
        self.builder.produce_part_decryption()
