"""
    Implement a pop method for the DynamicArray class, that removes the last element of the array,
    and that shrinks the capacity, N, of the array by half any time the number of elements in the
    array goes below N/4.
"""

import ctypes  # provides a low-level arrays


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
            self._resize(2 * self._capacity)  # so double capacity
        self._A[self._n] = obj
        self._n += 1

    def insert(self, k, value):
        """Insert a value at index k, shifting subsequent values rightward."""
        # we assume 0 <= k <= n
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
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
                self._n -= 1  # one less item
                return  # exit immediately
        raise ValueError('value not found')  # only reached if no match

    def pop(self):
        """
            Removes the last element of the array, and that shrinks the capacity, N,
            of the array by half any time the number of elements in the array goes below N/4.
        """
        try:
            self.remove(self._A[self._n - 1])
            if self._n >= self._capacity // 4:
                pass
            else:
                self._resize(self._capacity // 2)
            return
        except ValueError:
            self.pop()

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
        return (c * ctypes.py_object)()  # see ctypes documentation

    @property
    def n(self):
        return self._n

    @property
    def capacity(self):
        return self._capacity


if __name__ == '__main__':

    array = DynamicArray()
    test = [1, 0, 8, -3, 23, 45, 65, 90, -89, 120, 340, 5]  # 12 elementos
    for i in range(len(test)):
        array.append(test[i])

    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
    array.pop()
    print(f'\nNumber of elements: {array.n} / Capacity of the array: {array.capacity}')
    for i in array:
        print(i, end=' ')
