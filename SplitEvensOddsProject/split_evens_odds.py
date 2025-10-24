from singly_linked_list import SinglyLinkedList, Node

class SplitEvensOdds(SinglyLinkedList):
    """Derived class that splits the current list into two:
       one containing even numbers, one containing odd numbers."""

    def split_even_odd(self):
        if self.is_empty():
            return None, None

        evens = SinglyLinkedList()
        odds = SinglyLinkedList()
        current = self.head

        while current:
            next_node = current.next
            current.next = None  # detach
            if current.data % 2 == 0:
                if evens.head is None:
                    evens.head = evens.tail = current
                else:
                    evens.tail.next = current
                    evens.tail = current
                evens.count += 1
            else:
                if odds.head is None:
                    odds.head = odds.tail = current
                else:
                    odds.tail.next = current
                    odds.tail = current
                odds.count += 1
            current = next_node

        # clear the original list
        self.head = self.tail = None
        self.count = 0
        return evens, odds