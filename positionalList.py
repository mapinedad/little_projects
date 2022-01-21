from DoublyLinkedBase import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # -------------------------- nested Position class --------------------------

    class Position:
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)  # opposite of __eq__

    # ------------------------------- utility method -------------------------------

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be a proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    # ------------------------------- accessors -------------------------------

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        """Iterate PositionalList in reverse order."""
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)

    def _node_before(self, p):
        node = self._validate(p)
        before_p = self._make_position(self.before(p))._node
        return before_p

    def _node_after(self, p):
        node = self._validate(p)
        after_p = self._make_position(self.after(p))._node
        return after_p

    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node = self._validate(p)
        before_p = self._make_position(self.before(p))
        return before_p

    def after(self, p):
        """Return the Position just after Position p (or None if p is first)."""
        node = self._validate(p)
        after_p = self._make_position(self.before(p))
        return after_p

    def max(self):
        """Find the maximum value in the PositionalList and return that value."""
        maximum_value = self.first().element()
        for e in self:
            if e > maximum_value:
                maximum_value = e
            else:
                continue
        return maximum_value

    def find(self, e):
        """Find the position of element e within PositionalList, return None if e is not found."""
        self.sort(self)
        for element in self:
            if element != e:
                continue
            elif not (element != e):
                return self._make_position(e)
            else:
                return None

    # ------------------------------- mutators / update methods -------------------------------

    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p."""
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """
            Replace the element at Position p with e.
            Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element  # temporarily store old element
        original._element = e  # replace with new element
        return old_value

    def move_to_front(self, p):
        """
            Move an element of a list at position p to become
            the first element of the list (by relinking the existing node),
            while keeping the relative order of the remaining elements unchanged.
        """
        # page 295
        pass

    def swap(self, p, q):
        """
            Exchange the reference's of underlying nodes at p and q (both position),
            relinking the existing nodes and without creating any new node.
        """
        if self.is_empty():
            raise Empyt('Empty list!')
        else:
            if p == q:
                raise ValueError('p and q are same position!')
            else:
                node_before_p = self._node_before(p)
                node_after_p = self._node_after(p)
                node_before_q = self._node_before(q)
                node_after_q = self._node_after(q)

    @staticmethod
    def sort(pl):
        """Sort PositionalList of comparable elements into non-decreasing order."""
        if len(pl) > 1:
            marker = pl.first()
            while marker != pl.last():
                pivot = pl.after(marker)
                value = pivot.element()
                if value > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != pl.first() and pl.before(walk).element() > value:
                        walk = pl.before(walk)
                    pl.delete(pivot)
                    pl.add_before(walk, value)


if __name__ == '__main__':
    list_ = PositionalList()
    list_.add_first(192923)
    list_.add_first(-192923)
    list_.add_first(293)
    list_.add_last(90238)
    list_.add_last(-923)
    list_.add_last(13)
    list_.add_first(6454)
    list_.add_last(34545)

    for el in list_:
        print(el)

    list_.move_to_front(90238)

    for el in list_:
        print(el)

    """
    list_.sort(list_)

    print('PositionalList on increasing order:')
    for el in list_:
        print(el)

    print('\nPositionalList on reversed order:')
    for el in reversed(list_):
        print(el)
    """
