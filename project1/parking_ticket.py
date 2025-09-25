from __future__ import annotations
from math import ceil

class ParkingTicket:
    """
    Simulates a parking ticket.
    """

    BASE_FIRST_HOUR = 25.0
    ADDITIONAL_HOUR = 10.0

    def __init__(self, car, officer, illegal_minutes: int):
        self.car = car
        self.officer_name = getattr(officer, "name", str(officer))
        self.badge_number = getattr(officer, "badge_number", "")
        self.illegal_minutes = int(illegal_minutes)
        self.fine = self.calculate_fine()

    def calculate_fine(self) -> float:
        if self.illegal_minutes <= 0:
            return 0.0
        hours = ceil(self.illegal_minutes / 60)
        return self.BASE_FIRST_HOUR + self.ADDITIONAL_HOUR * (hours - 1)

    def __str__(self) -> str:
        lines = [
            "=== PARKING TICKET ===",
            f"Car       : {self.car.color} {self.car.make} {self.car.model} ({self.car.license_number})",
            f"Overtime  : {self.illegal_minutes} minutes",
            f"Fine      : ${self.fine:,.2f}",
            f"Issued by : Officer {self.officer_name} (Badge {self.badge_number})",
        ]
        return "\n".join(lines)