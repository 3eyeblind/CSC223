from dataclasses import dataclass


@dataclass(frozen=True)
class ScheduleItem:
   
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    instructor: str
    room: str
    mtg_start: str
    mtg_end: str
    days: str
    term: str

    @property
    def course_key(self) -> str:
        
        return f"{self.subject.strip().upper()}-{self.catalog.strip()}-{self.section.strip()}"

    @staticmethod
    def from_csv_row(row: dict) -> "ScheduleItem":
       
        return ScheduleItem(
            subject=row["Subject"].strip(),
            catalog=row["Catalog"].strip(),
            section=row["Section"].strip(),
            component=row["Component"].strip(),
            session=row["Session"].strip(),
            instructor=row["Instructor"].strip(),
            room=row["Room"].strip(),
            mtg_start=row["Mtg Start"].strip(),
            mtg_end=row["Mtg End"].strip(),
            days=row["Days"].strip(),
            term=row["Term"].strip(),
        )

  

    def matches_subject(self, subject: str) -> bool:
        return self.subject.upper() == subject.strip().upper()

    def matches_subject_catalog(self, subject: str, catalog: str) -> bool:
        return (
            self.subject.upper() == subject.strip().upper()
            and self.catalog.strip() == catalog.strip()
        )

    @property
    def instructor_last(self) -> str:
     
        parts = self.instructor.split(",", 1)
        if len(parts) >= 1:
            return parts[0].strip().upper()
        return self.instructor.strip().upper()

    def matches_instructor_last(self, last_name: str) -> bool:
        return self.instructor_last == last_name.strip().upper()

   

    def pretty_string(self) -> str:
      
       
        catalog_clean = self.catalog.strip()
        time_range = f"{self.mtg_start}–{self.mtg_end}" if self.mtg_start or self.mtg_end else ""
        room_part = f"Room {self.room}" if self.room else ""
        pieces = [
            f"{self.subject} {catalog_clean}-{self.section} ({self.component})",
            f"{self.days} {time_range}".strip(),
            room_part,
            self.instructor,
        ]
      
        return " | ".join(p for p in pieces if p)