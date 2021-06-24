#!/usr/bin/env python3

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
    self.items = []

  def __len__(self):
    return len(self.items)

  @property
  def length(self):
    return len(self.items)

  @staticmethod
  def left(i):
    return 2 * i + 1

  @staticmethod
  def right(i):
    return 2 * i + 2

  @staticmethod
  def parent(i):
    return (i - 1) // 2

  def _swap(self, i, j):
    self.items[i], self.items[j] = self.items[j], self.items[i]

  def _heapify(self, i):
    l = Heap.left(i)
    r = Heap.right(i)
    m = i

    if l < self.length and self.items[l] < self.items[m]:
      m = l
    if r < self.length and self.items[r] < self.items[m]:
      m = r

    if m != i:
      self._swap(m, i)
      self._heapify(m)

  def increase_priority(self, i, priority):
    if priority < self.items[i].priority:
      return
    self.items[i].priority = priority
    while i > 0 and self.items[Heap.parent(i)] > self.items[i]:
      self._swap(Heap.parent(i), i)
      i = Heap.parent(i)

  def top(self):
    return (self.items[0].priority, self.items[0].value) if self.length > 0 else None

  def get(self):
    if self.length == 0:
      return None
    self._swap(0, self.length - 1)
    item = self.items.pop()
    self._heapify(0)
    return (item.priority, item.value)

  def put(self, priority, value):
    self.items.append(HeapItem(float("-inf"), value))
    self.increase_priority(self.length - 1, priority)

heap = Heap()

if __name__ == "__main__":
  SIZE = 16
  for i in range(SIZE, -1, -1):
    heap.put(i, "aaa")

  for i in range(SIZE + 1):
    heap.put(i, "bbb")

  for i in range(2 * (SIZE + 1)):
    p, v = heap.get()
    assert p == i // 2


