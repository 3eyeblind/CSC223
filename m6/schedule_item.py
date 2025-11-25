from dataclasses import dataclass


@dataclass
class ScheduleItem:
    """
    Represents a single course section from the schedule.
    """
    subject: str       # e.g., "BIO"
    catalog: str       # e.g., "141"
    section: str       # e.g., "D01"
    component: str     # e.g., "DED", "LEC", "LAB"
    session: str       # e.g., "8W1", "10W", "DYN"
    units: int         # credit units
    tot_enrl: int      # total enrolled
    cap_enrl: int      # capacity
    instructor: str    # e.g., "Abrahams,Shaheem"

    def get_key(self) -> str:
        """
        Returns the unique key used in the Schedule dictionary.

        """
        return f"{self.subject}_{self.catalog}_{self.section}"

    def format_row(self) -> str:
       
        return (f"{self.subject:<7}"
                f"{self.catalog:<9}"
                f"{self.section:<9}"
                f"{self.component:<11}"
                f"{self.session:<9}"
                f"{self.units:>5}"
                f"{self.tot_enrl:>9}"
                f"{self.cap_enrl:>9}"
                f"  {self.instructor}")

    def print(self) -> None:
        """
        Prints the formatted row to the console.
        """
        print(self.format_row())