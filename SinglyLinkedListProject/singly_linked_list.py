from __future__ import annotations
from typing import Any, Iterable, Iterator, Optional, Tuple


class Node:
    __slots__ = ("data", "next")

    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["Node"] = None


class SinglyLinkedList:
    class EmptyListException(Exception):
        pass

    class NodeNotFoundException(Exception):
        pass

    def __init__(self):
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None
        self.__count: int = 0

    # ---------- Core utilities ----------
    def __len__(self) -> int:
        return self.__count

    def is_empty(self) -> bool:
        return self.__head is None

    def clear(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    def __iter__(self) -> Iterator[Any]:
        current = self.__head
        while current:
            yield current.data
            current = current.next

    def __append(self, value: Any) -> None:
        """O(1) append using tail pointer (forward build)."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            assert self.__tail is not None
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count += 1

    def __prepend(self, value: Any) -> None:
        """O(1) prepend to head (backward build)."""
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        if self.__tail is None:
            self.__tail = new_node
        self.__count += 1

    def build_forward_list(self, iterable: Iterable[Any]) -> None:
        """
        Preserves input order by appending to tail (forward).
        """
        for item in iterable:
            self.__append(item)

    def build_backward_list(self, iterable: Iterable[Any]) -> None:
        """
        Reverses input order by inserting at head (backward).
        """
        for item in iterable:
            self.__prepend(item)

    def insert_at_end(self, value: Any) -> None:
        """Alias for __append to align with assignment text."""
        self.__append(value)

    def insert_at_front(self, value: Any) -> None:
        self.__prepend(value)

    def insert_after(self, after_value: Any, new_value: Any) -> None:
        """Insert new_value after the first node whose data == after_value. O(n)."""
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException("insert_after on empty list")

        current = self.__head
        while current and current.data != after_value:
            current = current.next

        if current is None:
            raise SinglyLinkedList.NodeNotFoundException(
                f"value {after_value} not found"
            )

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
        if current is self.__tail:
            self.__tail = new_node
        self.__count += 1


    def remove_first(self) -> Any:
        """Remove head node. O(1)."""
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException("remove_first on empty list")
        value = self.__head.data
        self.__head = self.__head.next
        if self.__head is None:
            self.__tail = None
        self.__count -= 1
        return value

    def remove_last(self) -> Any:
        """Remove tail node. O(n) to find predecessor."""
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException("remove_last on empty list")

  
        if self.__head is self.__tail:
            value = self.__head.data
            self.__head = self.__tail = None
            self.__count = 0
            return value

        prev = self.__head
        while prev.next is not self.__tail:
            prev = prev.next 
        assert self.__tail is not None
        value = self.__tail.data
        prev.next = None
        self.__tail = prev
        self.__count -= 1
        return value

    def remove(self, value: Any) -> None:
        """Remove the first node whose data == value. O(n)."""
        if self.__head is None:
            raise SinglyLinkedList.EmptyListException("remove on empty list")

        current = self.__head
        previous = None

        while current and current.data != value:
            previous = current
            current = current.next

        if current is None:
            raise SinglyLinkedList.NodeNotFoundException(
                f"value {value} not found"
            )

        # Remove node
        if previous is None:
         
            self.__head = current.next
        else:
            previous.next = current.next

        if current is self.__tail:
            self.__tail = previous

        self.__count -= 1

    def remove_all(self, value: Any) -> int:
        """
        Remove all nodes whose data == value. O(n).
        Returns number of removed nodes.
        """
        if self.__head is None:
            return 0

        removed = 0
        dummy = Node(None)
        dummy.next = self.__head
        prev = dummy
        cur = self.__head

        while cur:
            if cur.data == value:
                prev.next = cur.next
                removed += 1
                self.__count -= 1
                if cur is self.__tail:
                    self.__tail = prev if prev is not dummy else None
                cur = prev.next
            else:
                prev = cur
                cur = cur.next

        self.__head = dummy.next
        if self.__head is None:
            self.__tail = None
        return removed

    # ---------- Displays ----------
    def display(self) -> None:
        """
        Print in the form: Head -> a -> b -> ... -> None
        """
        parts = ["Head"]
        cur = self.__head
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        parts.append("None")
        print(" -> ".join(parts))

    def display_reverse(self) -> None:
        """
        Recursive reverse display (does not modify the list).
        """
        def _collect_rev(node: Optional[Node]) -> list:
            return _collect_rev(node.next) + [node.data] if node else []

        items = _collect_rev(self.__head)
       
        left = ["None"]
        right = list(map(str, items)) + ["Head"]
        print(" <- ".join(left + right))

    def display_reverse_nr(self) -> None:
        """
        Non-recursive reverse display using an explicit stack (list). O(n) time, O(n) space.
        Does not modify the list.
        """
        stack = []
        cur = self.__head
        while cur:
            stack.append(cur.data)
            cur = cur.next
  
        parts = ["None"]
        while stack:
            parts.append(str(stack.pop()))
        parts.append("Head")
        print(" <- ".join(parts))