from __future__ import annotations
from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, s: float, n: str = "Square"):
        self._side: float = float(s)
        super().__init__(s, s, n)
        self.name = n

    @property
    def side(self) -> float:
        return self._side

    @side.setter
    def side(self, value: float) -> None:
        self._side = float(value)
        self.length = self._side
        self.width = self._side

    def __str__(self) -> str:
        return f"{self.name} Area = {self.area:g}"