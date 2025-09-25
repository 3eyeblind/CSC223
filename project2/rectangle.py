from __future__ import annotations
from basic_shape import BasicShape

class Rectangle(BasicShape):
    def __init__(self, l: float, w: float, n: str = "Rectangle"):
        super().__init__(n)
        self._length: float = float(l)
        self._width: float = float(w)
        self.calc_area()

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, value: float) -> None:
        self._length = float(value)
        self.calc_area()

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        self._width = float(value)
        self.calc_area()

    def calc_area(self) -> None:
        self._set_area(self._length * self._width)

    def __str__(self) -> str:
        return f"{self.name} Area = {self.area:g}"