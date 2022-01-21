from sys import path

path.append('..\\Git_files')

from Git_files.ArrayStack import Empty


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    # -------------------------- nested _Node class --------------------------

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'

        def __init__(self, element, next_):     # initialize node's fields
            self._element = element             # reference to user's element
            self._next = next_                  # reference to next node

    def __init__(self):
        self._tail = None       # will represent tail of queue
        self._size = 0          # current number of elements in queue

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def firs(self):
        if self.is_empty():
            raise Empty('Empty Queue!')
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty('Empty Queue!')
        oldhead = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
