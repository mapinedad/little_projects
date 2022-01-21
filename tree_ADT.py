"""Abstract base class Tree defined here"""

class Tree:
	
	"""This is an abstract base class representing a Tree ADT"""

	# ---------------------- nested Position class -----------------------

	class Position:
		
		"""Abstraction representing the location of a single element"""

		def element(self):
			"""Return the element stored at this Position."""
			raise NotImplementedError('must be implemented by subclass')

		def __eq__(self, other):
			"""Return True if other Position represents the same location."""
			raise NotImplementedError('must be implemented by subclass')

		def __ne__(self, other):
			"""Return True if other does not represent the same location."""
			return not (self == other)

	# Here are defined the abstract methods that concrete subclass must support

	def root(self):
		"""Return position representing the Tree's root or None if Tree is empty."""
		raise NotImplementedError('must be implemented by subclass')

	def parent(self, p):
		"""Return Position representing p's parent or None if p is root."""
		raise NotImplementedError('must be implemented by subclass')

	def num_children(self, p):
		"""Return the number of children that Position p has."""
		raise NotImplementedError('must be implemented by subclass')

	def children(self, p):
		"""Generate an iteration of Positions representing p's children."""
		raise NotImplementedError('must be implemented by subclass')

	def __len__(self):
		"""Return the total number of elements in the Tree"""
		raise NotImplementedError('must be implemented by subclass')

	# Here are the concrete methods implemented in this class

	def is_root(self, p):
		"""Return True if Position p represents the root of the Tree"""
		return self.root() == p

	def is_leaf(self, p):
		"""Return True if p not have any children."""
		return self.num_children(p) == 0

	def is_empty(self):
		"""Return True if the tree is empty."""
		return len(self) == 0

	# utility for compute the depth and height

	def depth(self, p):
		"""Return the number of levels separating Position p from the root."""
		if self.is_root(p):
			return 0
		else:
			return 1 + self.depth(self.parent(p))	# recursive step

	def _height(self, p):
		"""Return the height of the subtree rooted at Position p."""
		if self.is_leaf(p):
			return 0
		else:
			return 1 + max(self._height(c) for c in self.children(p))

	# the public utility version which use the _height method for compute the height of a tree

	def height(self, p=None):
		"""Return the height of the subtree rooted at Position p.
		   If p is None, return the height of the entire tree."""
		if p is None:
			p = self.root()
		return self._height(p)	# begin the recursion


# ------------------------------------- BinaryTree ADT ---------------------------------------


class BinaryTree(Tree): # inherit from Tree ADT

	# ---------------------- additional abstract methods -----------------------

	def left(self, p):
		"""Return the position that represents the left child of p,
		   or None if p has no left child."""
		raise NotImplementedError('must be implemented by subclass')

	def right(self, p):
		"""Return the position that represents the right child of p,
		   or None if p has no right child."""
		raise NotImplementedError('must be implemented by subclass')

	# ---------------------- methods implemented -----------------------

	def sibling(self, p):
		"""Return the position that represents the sibling of p,
		   or None if p has no siblings."""
		parent = self.parent(p)

		if parent is None:
			return None
		else:
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)

	def children(self, p):
		"""Generate an iteration of Positions representing p's children."""
		if self.left(p) is not None:
			yield self.left(p)
		if self.right(p) is not None:
			yield self.right(p)


# ------------------------------------- LinkedBinaryTree ---------------------------------------


class LinkedBinaryTree(BinaryTree):

	"""Representation of a BinaryTree based on linked structure."""

	class _Node:

		__slots__ = '_element', '_parent', '_left', '_right'

		def __init__(self, element, parent=None, left=None, right=None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right

	class Position(BinaryTree.Position):
		"""Abstraction which represent the location of a single element."""

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

		def _validate(self, p):
			"""Return associated node, if position p is valid."""
			if not isinstance(p, self.Position):
				raise TypeError('p must be proper Position type')
			if p._container is not self:
				raise ValueError('p does not belong to this container')
			if p._node._parent is p._node:		# for deprecated node
				raise ValueError('p is no longer valid ')
			return p._node

		def _make_position(self, node):
			"""Return Position instance for given node
			   None if no node."""
			return self.Position(self, node) if node is not None else None

	# ----------------------------- BinaryTree constructor -----------------------------

	def __init__(self):
		"""Initially empty binary Tree"""
		self._root = None
		self._size = 0

	# accesors public methods

	def __len__(self):
		"""Return the total number of elements in the tree"""
		return self._size

	def root(self):
		"""if BinaryTree is not empty return the Position of the root.
		   otherwise, return None."""
		return self._make_position(self._root)

	def parent(self, p):
		"""Return the position of p's parent. If p is the tree's root return None."""
		node = self._validate(p)
		return self._make_position(node._parent)

	def left(self, p):
		"""Return the position of p's left child. None if p doesn't have anyone."""
		node = self._validate(p)
		return self._make_position(node._left)

	def right(self, p):
		"""Return the position of p's right child. None if p doesn't have anyone."""
		node = self._validate(p)
		return self._make_position(node._right)

	def num_children(self, p):
		"""Return the number of children of Position p"""
		node = self._validate(p)
		count = 0
		if node._left is not None:		# p have a left child
			count += 1
		if node._right is not None:		# p have a right child
			count += 1
		return count

	def _add_root(self, e):
		"""Place element e at the root of an empty tree and return new Position.
			Raise ValueError if the tree is not empty."""
		if self._root is not None:
			raise ValueError('Root exists')
		self._size = 1
		self._root = self._Node(e)
		return self._make_position(self._root)

	def _add_left(self, p, e):
		"""Create a new left child for Position p, storing element e.

			Return the position of new node.
			Raise ValueError if Position p is invalid or p already has a left child.
		"""
		node = self._validate(p)
		if node._left is not None:
			raise ValueError('Left child already exist')
		self._size += 1
		node._left = self._Node(e, node)
		return self._make_position(node._left)

	def _add_right(self, p, e):
		"""Create a new right child for Position p, storing element e.

			Return the position of new node.
			Raise ValueError if Position p is invalid or p already has a right child.
		"""
		node = self._validate(p)
		if node._right is not None:
			raise ValueError('Right child already exist')
		self._size += 1
		node._right = self._Node(e, node)
		return self._make_position(node._right)

	def _replace(self, p, e):
		"""Replace the element at position p with e and return the old element."""
		node = self._validate(p)
		old_element = node._element
		node._element = e
		return old_element

	def _delete(self, p):
		"""Delete the node at Position p, and replace it with its child, if any.

			Return the element that had been stored at Position p.
			Raise ValueError if Position p is invalid or p has two children.
		"""
		node = self._validate(p)

		if self.num_children(p) == 2:
			raise ValueError('p has two children')

		if node._left:
			child = node._left
		else:
			child = node._right

		if child is not None:
			child._parent = node._parent
		
		if node is self._root:
			self._root = child
		else:
			parent = node._parent
			
			if node is parent._left:
				parent.left = child
			else:
				parent._right = child
		self._size -= 1
		node._parent = node 	# convention for deprecated node
		return node._element

	def _attach(self, p, t1, t2):
		"""Attach trees t1 and t2 as left and right (respectively) subtrees of external p."""
		node = self._validate(p)

		if not self.is_leaf(p):
			raise ValueError('position must be leaf')

		if not type(self) is type(t1) is type(t2):		# must be the same type
			raise TypeError('Tree types must catch')

		self._size += len(t1) + len(t2)

		if not t1.is_empty():		# t1 will be the left subtree of node
			t1._root._parent = node
			node._left = t1._root
			t1._root = None
			t1._size = 0

		if not t2.is_empty():		# t2 will be the right subtree of node
			t2._root._parent = node
			node._right = t2._root
			t2._root = None
			t2._size = 0
