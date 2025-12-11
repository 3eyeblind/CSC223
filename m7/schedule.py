import csv
from typing import Iterable, List, Tuple, Callable

from schedule_item import ScheduleItem
from search_trees import BSTMap, AVLTreeMap


class CourseSchedule:
   

    def __init__(self, backend: str = "bst"):
        backend = backend.lower()
        if backend == "bst":
            self._tree = BSTMap()
        elif backend == "avl":
            self._tree = AVLTreeMap()
        else:
            raise ValueError("backend must be 'bst' or 'avl'")

        self._count = 0  


    def load_from_csv(self, filename: str) -> None:
        """
        Load data from courses_2023.csv using DictReader.
        Uses utf-8-sig to handle BOM if present.
        """
        self._tree = type(self._tree)()  
        self._count = 0

        with open(filename, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                item = ScheduleItem.from_csv_row(row)
               
                self._tree.insert(item.course_key, item)
                self._count += 1

    def record_count(self) -> int:
        """Return how many schedule items are stored in this schedule."""
        return self._count

   

    def _iter_items(self) -> Iterable[Tuple[str, ScheduleItem]]:
        """Iterate over (key, item) pairs via inorder traversal."""
        yield from self._tree.inorder_items()

    def _filter_items(self, predicate: Callable[[ScheduleItem], bool]) -> List[ScheduleItem]:
        """Return a list of items matching a given predicate."""
        results: List[ScheduleItem] = []
        for _key, item in self._iter_items():
            if predicate(item):
                results.append(item)
        return results

   

    def all_items(self) -> List[ScheduleItem]:
        """Return all schedule items in sorted key order."""
        return [item for _key, item in self._iter_items()]

    def search_by_subject(self, subject: str) -> List[ScheduleItem]:
        """Return all courses matching a given subject."""
        return self._filter_items(lambda item: item.matches_subject(subject))

    def search_by_subject_catalog(self, subject: str, catalog: str) -> List[ScheduleItem]:
        """Return all courses matching subject + catalog number."""
        return self._filter_items(lambda item: item.matches_subject_catalog(subject, catalog))

    def search_by_instructor_last(self, last_name: str) -> List[ScheduleItem]:
        """Return all courses taught by an instructor (last name)."""
        return self._filter_items(lambda item: item.matches_instructor_last(last_name))



    def tree_height(self) -> int:
        """
        Return height of underlying tree (delegates to BST/AVL height()).
        Height = number of edges on longest root-to-leaf path.
        """
        return self._tree.height()

   

    @staticmethod
    def format_items(items: List[ScheduleItem]) -> str:
        """Return a multi-line string of pretty-printed items."""
        if not items:
            return "No matching courses found."
        lines = [item.pretty_string() for item in items]
        return "\n".join(lines)