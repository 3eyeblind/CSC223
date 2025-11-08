from dataclasses import dataclass
import heapq
from typing import Optional, ClassVar, Tuple


@dataclass(order=True)
class _Entry:
   
    priority: Tuple[int, int]
    name: str
    severity: int

class TriageSystem:
    _arrival_counter: ClassVar[int] = 0  # class-level static counter 

    def __init__(self):
        self._heap: list[_Entry] = []

    @classmethod
    def NextArrivalOrder(cls) -> int:
        val = cls._arrival_counter
        cls._arrival_counter += 1
        return val

    def AddPatient(self, name: str, severity: int) -> None:
        if not name or not isinstance(name, str):
            raise ValueError("Invalid name")
        if not (1 <= severity <= 5):
            raise ValueError("Severity must be in 1..5")
        arrival = TriageSystem.NextArrivalOrder()
       
        entry = _Entry(priority=(-severity, arrival), name=name, severity=severity)
        heapq.heappush(self._heap, entry)  

    def ProcessNext(self) -> Optional[tuple[str, int]]:
        if not self._heap:
            return None
        e = heapq.heappop(self._heap)      
        return (e.name, e.severity)

    def PeekNext(self) -> Optional[tuple[str, int]]:
        if not self._heap:
            return None
        e = self._heap[0]                   
        return (e.name, e.severity)

    def IsEmpty(self) -> bool:
        return not self._heap

    def Size(self) -> int:
        return len(self._heap)

    def Clear(self) -> None:
        self._heap.clear()

   
    def load(self, items: list[tuple[str, int]]) -> None:
        for name, sev in items:
            self.AddPatient(name, sev)