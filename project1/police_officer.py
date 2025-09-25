from __future__ import annotations
from typing import Optional
from parking_ticket import ParkingTicket

class PoliceOfficer:
    """Simulates a police officer inspecting parked cars."""

    def __init__(self, name: str, badge_number: str):
        self.name = str(name)
        self.badge_number = str(badge_number)

    def inspect_car(self, car, meter) -> Optional[ParkingTicket]:
        illegal = car.minutes_parked - meter.minutes_purchased
        if illegal > 0:
            return ParkingTicket(car, self, illegal)
        return None

    def __str__(self) -> str:
        return f"Officer {self.name} (Badge {self.badge_number})"