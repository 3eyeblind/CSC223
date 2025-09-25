from __future__ import annotations
from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name: str = "Shape"):
        self._name: str = name
        self._area: float = 0.0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = str(value)

    @property
    def area(self) -> float:
        return self._area

    def _set_area(self, value: float) -> None:
        self._area = float(value)

    @abstractmethod
    def calc_area(self) -> None:
        raise NotImplementedError