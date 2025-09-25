from __future__ import annotations

class ParkingMeter:
    """Simulates a parking meter with purchased time."""

    def __init__(self, minutes_purchased: int = 60):
        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self) -> int:
        return self.__minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes: int) -> None:
        if not isinstance(minutes, int):
            raise TypeError("minutes_purchased must be an int")
        if minutes <= 0:
            raise ValueError("minutes_purchased must be > 0")
        self.__minutes_purchased = minutes

    def __str__(self) -> str:
        return f"Meter: {self.minutes_purchased} minutes purchased"