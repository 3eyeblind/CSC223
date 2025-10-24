class Stack:
    """
    Adapter over Python's list that exposes only stack operations (LIFO).

    Methods:
        push(item)  -> None
        pop()       -> item      (raises IndexError if empty)
        peek()      -> item      (raises IndexError if empty)
        is_empty()  -> bool
        size()      -> int
    """
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)  

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()  

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)