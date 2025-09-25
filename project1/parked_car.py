from __future__ import annotations

class ParkedCar:
    """
    Simulates a parked car.
    Public identity fields; private minutes_parked with validation through @property.
    """

    def __init__(self, make: str, model: str, color: str, license_number: str, minutes_parked: int = 60):
        self.make = str(make)
        self.model = str(model)
        self.color = str(color)
        self.license_number = str(license_number)
        self.minutes_parked = minutes_parked  # uses setter validation

    @property
    def minutes_parked(self) -> int:
        return self.__minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes: int) -> None:
        if not isinstance(minutes, int):
            raise TypeError("minutes_parked must be an int")
        if minutes <= 0:
            raise ValueError("minutes_parked must be > 0")
        self.__minutes_parked = minutes

    def __str__(self) -> str:
        return f"{self.color} {self.make} {self.model} ({self.license_number}) — parked {self.minutes_parked} min"