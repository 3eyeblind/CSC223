import csv
from typing import Dict, List
from schedule_item import ScheduleItem


class Schedule:
    """
    Holds all ScheduleItem objects in a dictionary keyed by
    SUBJECT_CATALOG_SECTION 
    """

    def __init__(self) -> None:
        # key: str 
        # value: ScheduleItem
        self._items: Dict[str, ScheduleItem] = {}

    # Basic dictionary operations

    def add_entry(self, item: ScheduleItem) -> None:
        """
        Adds a ScheduleItem to the internal dictionary using its key.
        If a key already exists, it will be replaced with the new item.
        """
        key = item.get_key()
        self._items[key] = item

    def __len__(self) -> int:
        return len(self._items)

    
    # CSV loading
    

    @staticmethod
    def _safe_int(value: str, default: int = 0) -> int:
        """
        Convert a string to int, returning default if it's empty or invalid.
        """
        value = value.strip()
        if value == "":
            return default
        try:
            return int(value)
        except ValueError:
            return default

    def load_from_csv(self, filename: str) -> None:
        """
        Loads schedule data from a CSV file using csv.DictReader.

        Expected columns (at minimum):
        Subject, Catalog, Section, Component, Session,
        Units, TotEnrl, CapEnrl, Instructor
        """
        with open(filename, encoding="utf-8-sig", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Skip empty lines or malformed rows
                subject = row.get("Subject", "").strip()
                if not subject:
                    continue

                catalog = row.get("Catalog", "").strip()
                section = row.get("Section", "").strip()
                component = row.get("Component", "").strip()
                session = row.get("Session", "").strip()

                units = self._safe_int(row.get("Units", "0"))
                tot_enrl = self._safe_int(row.get("TotEnrl", "0"))
                cap_enrl = self._safe_int(row.get("CapEnrl", "0"))

                instructor = row.get("Instructor", "").strip()

                item = ScheduleItem(
                    subject=subject,
                    catalog=catalog,
                    section=section,
                    component=component,
                    session=session,
                    units=units,
                    tot_enrl=tot_enrl,
                    cap_enrl=cap_enrl,
                    instructor=instructor,
                )

                self.add_entry(item)

    
    # Printing 
    

    def print_header(self) -> None:
        """
        Prints a header row for the schedule report.
        """
        header = (
            f"{'Subject':<7}"
            f"{'Catalog':<9}"
            f"{'Section':<9}"
            f"{'Component':<11}"
            f"{'Session':<9}"
            f"{'Units':>5}"
            f"{'TotEnrl':>9}"
            f"{'CapEnrl':>9}"
            f"  {'Instructor'}"
        )
        print(header)
        print("-" * len(header))

    def print(self, items: List[ScheduleItem] = None) -> None:
        """
        Prints either:
        - all schedule items (if items is None), or
        - the given list of ScheduleItem objects.
        """
        if items is None:
            items = list(self._items.values())

        self.print_header()
        for item in items:
            item.print()

    
    # Helper for instructor last name
    

    @staticmethod
    def _extract_last_name(full_name: str) -> str:
        """
        Extracts the last name from the Instructor field.
       
        """
        if not full_name:
            return ""

        before_comma = full_name.split(",", 1)[0].strip()
        if not before_comma:
            return ""

        # In cases like "Anderson Jr.", use the first token as the base last name
        tokens = before_comma.split()
        if not tokens:
            return before_comma

        base_last = tokens[0]
        return base_last

    
    # Search / filter methods (using list comprehensions)
    

    def find_by_subject(self, subject: str) -> List[ScheduleItem]:
        """
        Returns a list of ScheduleItem objects matching the given subject.
        Case-insensitive.
        """
        subject = subject.strip().upper()
        return [
            item
            for item in self._items.values()
            if item.subject.upper() == subject
        ]

    def find_by_subject_catalog(self, subject: str, catalog: str) -> List[ScheduleItem]:
        """
        Returns a list of ScheduleItem objects matching subject and catalog.
        Case-insensitive.
        """
        subject = subject.strip().upper()
        catalog = catalog.strip()
        return [
            item
            for item in self._items.values()
            if item.subject.upper() == subject and item.catalog == catalog
        ]

    def find_by_instructor_last_name(self, last_name: str) -> List[ScheduleItem]:
        """
        Returns a list of ScheduleItem objects where the instructor's last name
        matches the given last_name (case-insensitive).

        """
        last_name = last_name.strip().lower()
        return [
            item
            for item in self._items.values()
            if self._extract_last_name(item.instructor).lower() == last_name
        ]