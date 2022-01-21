"""
    This .py file contain the definition of ArrayStack class, which emulate some behaviors of ADT STACK.
    The class itself rely on builtin python data structure List.
"""


class Empty(Exception):
    pass


class ArrayStack:
    """LIFO stack implementation using a Python list as underlying storage."""
    def __init__(self):
        """Create a empty Stack"""
        self._data = []     # rely on list

    def __len__(self) -> object:
        """Return the length of ArrayStack instance"""
        return len(self._data)

    def is_empty(self) -> bool:
        """Check if the stack is empty. 
           Return True, otherwise False.
        """
        return len(self._data) == 0

    def push(self, e):
        """Add element on the stack"""
        self._data.append(e)

    def top(self) -> object:
        """Return but not remove the top element on the stack (the last element on the underlying list)"""
        if self.is_empty():     # check if stack is empty
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self) -> object:
        """Remove and return the stack's top element. (the last element on the underlying list)"""
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def __str__(self) -> str:
        """Represent the stack as str"""
        return str(self._data)
