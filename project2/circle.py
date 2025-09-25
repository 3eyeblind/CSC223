from __future__ import annotations
from math import pi
from basic_shape import BasicShape

class Circle(BasicShape):
    def __init__(self, x: float, y: float, r: float, n: str = "Circle"):
        super().__init__(n)
        self._x_center: float = float(x)
        self._y_center: float = float(y)
        self._radius: float = float(r)
        self.calc_area()

    @property
    def x_center(self) -> float:
        return self._x_center

    @property
    def y_center(self) -> float:
        return self._y_center

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        self._radius = float(value)
        self.calc_area()

    def calc_area(self) -> None:
        self._set_area(pi * (self._radius ** 2))

    def __str__(self) -> str:
        return f"{self.name} Area = {self.area:.5f}"