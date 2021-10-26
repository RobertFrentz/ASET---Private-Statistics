from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Protocol1:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Protocol parts: {','.join(self.parts)}", end="")
