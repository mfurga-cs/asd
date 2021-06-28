
def g_convert(desc, matrix=False, directed=False):
  """
  TGF converter.
  """
  G = None
  vertices = 0
  phaze = 0
  for line in desc.strip().splitlines():
    if line == "#":
      if matrix:
        G = [[0] * vertices for _ in range(vertices)]
      else:
        G = [[] for i in range(vertices)]
      phaze = 1
      continue
    if phaze == 0:
      vertices += 1
    if phaze == 1:
      u, v, w = map(int, (line.split() + [1])[:3])
      if matrix:
        G[u][v] = w
        if not directed:
          G[v][u] = w
      else:
        G[u].append((v, w))
        if not directed:
          G[v].append((u, w))
  return G

class HeapItem:
  def __init__(self, priority: int, value: object):
    self.priority = priority
    self.value = value

  def __lt__(self, other):
    return self.priority < other.priority

  def __eq__(self, other):
    return self.priority == other.priority

class Heap:
  """
  Min-heap implementation.
  """
  def __init__(self):
    self._items = []

  def __len__(self):
    return len(self._items)

  @property
  def length(self):
    return len(self._items)

  @staticmethod
  def _left(i):
    return 2 * i + 1

  @staticmethod
  def _right(i):
    return 2 * i + 2

  @staticmethod
  def _parent(i):
    return (i - 1) // 2

  def _swap(self, i, j):
    self._items[i], self._items[j] = self._items[j], self._items[i]

  def _heapify(self, i):
    l = Heap._left(i)
    r = Heap._right(i)
    m = i

    if l < self.length and self._items[l] < self._items[m]:
      m = l
    if r < self.length and self._items[r] < self._items[m]:
      m = r

    if m != i:
      self._swap(m, i)
      self._heapify(m)

  def increase_priority(self, i, priority):
    if priority < self._items[i].priority:
      return
    self._items[i].priority = priority
    while i > 0 and self._items[Heap._parent(i)] > self._items[i]:
      self._swap(Heap._parent(i), i)
      i = Heap._parent(i)

  def top(self):
    return (self._items[0].priority, self._items[0].value) if self.length > 0 else None

  def get(self):
    if self.length == 0:
      return None
    self._swap(0, self.length - 1)
    item = self._items.pop()
    self._heapify(0)
    return (item.priority, item.value)

  def put(self, priority, value):
    self._items.append(HeapItem(float("-inf"), value))
    self.increase_priority(self.length - 1, priority)

class BSTNode:
  def __init__(self, value, parent=None):
    self.value = value
    self.parent = parent
    self.lchild = None
    self.rchild = None

class BST:
  def __init__(self):
    self._root = None

  def __repr__(self):
    return self._print_tree(self._root)

  def _print_tree(self, node, level=0):
    result = ""
    if node != None:
      result += self._print_tree(node.rchild, level + 1)
      result += "{value: >{width}}\n".format(value=node.value, width=4*level)
      result += self._print_tree(node.lchild, level + 1)
    return result

  def find(self, value):
    curr = self._root
    while curr is not None and curr.value != value:
      if curr.value > value:
        curr = curr.lchild
      else:
        curr = curr.rchild
    return curr

  def _min(self, node):
    while node.lchild is not None:
      node = node.lchild
    return node

  def min(self):
    if self._root is None:
      return None
    return self._min(self._root)

  def _max(self, node):
    while node.rchild is not None:
      node = node.rchild
    return node

  def max(self):
    if self._root is None:
      return None
    return self._max(self._root)

  def insert(self, value):
    if self._root is None:
      self._root = BSTNode(value)
      return
    curr = self._root
    while True:
      if curr.value > value:
        if curr.lchild is None:
          curr.lchild = BSTNode(value, curr)
          break
        curr = curr.lchild
      else:
        if curr.rchild is None:
          curr.rchild = BSTNode(value, curr)
          break
        curr = curr.rchild

  def _transplant(self, u, v):
    if u.parent == None:
      self._root = v
    elif u == u.parent.lchild:
      u.parent.lchild = v
    else:
      u.parent.rchild = v
    if v != None:
      v.parent = u.parent

  def delete(self, value):
    z = self.find(value)
    if z is None:
      return

    if z.lchild is None:
      self._transplant(z, z.rchild)
    elif z.rchild is None:
      self._transplant(z, z.lchild)
    else:
      y = self._min(z.rchild)
      if y.parent != z:
        self._transplant(y, y.rchild)
        y.rchild = z.rchild
        y.rchild.parent = y
      self._transplant(z, y)
      y.lchild = z.lchild
      y.lchild.parent = y

  def successor(self, value):
    x = self.find(value)
    if x is None:
      return
    if x.rchild is not None:
      return self._min(x.rchild)
    y = x.parent
    while y is not None and x == y.rchild:
      x = y
      y = y.parent
    return y

  def predecessor(self, value):
    x = self.find(value)
    if x is None:
      return
    if x.lchild is not None:
      return self._max(x.lchild)
    y = x.parent
    while y is not None and x == y.lchild:
      x = y
      y = y.parent
    return y


