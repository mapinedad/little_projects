"""
    C-5.15 Consider an implementation of a dynamic array, but instead of copying
    the elements into an array of double the size (that is, from N to 2N) when
    its capacity is reached, we copy the elements into an array with
    ceil(N/4) additional cells, going from capacity N to capacity N + ceil(N/4). Prove that
    performing a sequence of n append operations still runs in O(n) time in this case.
"""

from time import time_ns
import ctypes  # provides a low-level arrays
from math import ceil


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not abs(k) < self._n:
            raise IndexError('Invalid index')
        elif self._n > 0 <= k:
            return self._A[k]  # retrieve from array
        elif k < 0:
            return self._A[self._n + k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(ceil(self._capacity / 4) + self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert a value at index k, shifting subsequent values rightward."""
        # we assume 0 <= k <= n
        if self._n == self._capacity:   # not enough room
            self._resize(2 * self._capacity)    # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._A[j] = self._A[j - 1]
        self._A[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value (or Raise ValueError)."""
        # note: we do not considering shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:  # found a match
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1    # one less item
                return  # exit immediately
            raise ValueError('value not found')  # only reached if no match

    def _resize(self, c):  # nonpublic utility
        """Resize internal array to capacity c."""
        B = self._make_array(c)  # new -bigger- array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._A = B  # use the bigger array
        self._capacity = c

    @staticmethod
    def _make_array(c):  # nonpublic utility
        """Return new array with capacity c."""
        return (c * ctypes.py_object)()     # see ctypes documentation


# Testing the new DynamicArray
start = time_ns()
array = DynamicArray()
for i in range(1000000):
    array.append(i)

end = time_ns()

print(f'The elapsed time in nanoseconds is {(end-start)/(10**9)}')