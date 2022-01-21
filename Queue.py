"""
    Simple adapter that implements queue ADT while using a
    collections.deque instance for storage.
"""

from collections import deque as dq


class Queue(dq):
    """ A queue class that inherit from collections.deque """

    def __init__(self):
        super().__init__()
        self._data = dq()
        self._size = 0
        self._front = 0

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    @property
    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        try:
            return self[self._front]
        except IndexError as error:
            print(error)

    def enqueue(self, e):
        """Add an element to the back of queue"""
        self.append(e)
        self._size += 1

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        try:
            return self.popleft()
        except IndexError as error:
            print(error)
