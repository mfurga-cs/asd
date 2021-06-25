
def tgf_conv(desc, directed=False):
  """
  TGF converter to matrix reprezentation. Assume verteces are labed from 0 to n.
  """
  G = None
  vertices = 0
  phaze = 0
  for line in desc.strip().splitlines():
    if line == "#":
      G = [[0] * vertices for _ in range(vertices)]
      phaze = 1
      continue
    if phaze == 0:
      vertices += 1
    if phaze == 1:
      u, v, w = map(int, (line.split() + [1])[:3])
      G[u][v] = w
      if directed:
        G[v][u] = w
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

