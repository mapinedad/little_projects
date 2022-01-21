from sys import path

path.append('..\\Git_files')
from Git_files.ArrayStack import Empty


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next_):
            self._element = element
            self._prev = prev
            self._next = next_

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer      # trailer is after header
        self._trailer._prev = self._header      # header is before trailer
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def __iter__(self):
        current = self._header._next
        for _ in range(self._size):
            yield current._element
            current = current._next

    def reverse(self):
        """Reverses the order of the list, yet without creating or destroying any nodes."""
        last = self._trailer._prev
        for _ in self:
            yield last._element
            last = last._prev

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element     # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element


# ------------------------------- Deque based on LinkedList -------------------------------


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty!')
        else:
            return self._header._next._element

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty!')
        else:
            return self._trailer._prev._element

    def insert_first(self, e):
        """Insert element e to the front of the deque."""
        self._insert_between(e, self._header, self._header._next)     # after header

    def insert_last(self, e):
        """Insert element e to the back of the deque."""
        self._insert_between(e, self._trailer._prev, self._trailer)   # before trailer

    def delete_first(self):
        """
            Remove and return the element at the front of the deque.
            Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._header._next)

    def delete_last(self):
        """
            Remove and return the element at the back of the deque.
            Raise Empty exception if the deque is empty.
        """
        if self.is_empty():
            raise Empty('Deque is empty!')
        return self._delete_node(self._trailer._prev)


if __name__ == '__main__':

    deque = LinkedDeque()
    deque.insert_first('Aloha')
    deque.insert_last('Terminator')
    deque.insert_first('Camila')
    deque.insert_last('Banana')
    deque.insert_first('Lola')

    for i in deque:
        print(i, end=' ')

    print("\nReversed deque:")
    for i in deque.reverse():
        print(i, end=' ')
