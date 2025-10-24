from typing import Any, Optional

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None


class SinglyLinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.count = 0

    def is_empty(self) -> bool:
        return self.head is None

    def build_forward_list(self, data_list):
        for item in data_list:
            new_node = Node(item)
            if not self.head:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.count += 1

    def remove_first(self):
        if self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            self.count -= 1

    def display(self):
        current = self.head
        print("Head -> ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")