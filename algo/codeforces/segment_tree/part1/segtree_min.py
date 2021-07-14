#!/usr/bin/env python3
#
# Segment Tree based on array.
# 1. set(i, v) - set the value to given index.
# 2. min(a, b) - min on the segment from a to b.

def _next_pow_2(n):
  i = 1
  while i < n:
    i *= 2
  return i

class SegmentTree:
  def __init__(self, n):
    self._size = _next_pow_2(n)
    self._array = [0] * self._size * 2

  @classmethod
  def build(cls, array):
    n = len(array)
    self = cls(n)
    i = self._size - 1
    j = 0
    while j < n:
      self._array[i] = array[j]
      i += 1
      j += 1
    self._repair(0)
    return self

  def _repair(self, vertex):
    if vertex >= self._size - 1:
      return
    self._repair(vertex * 2 + 1)
    self._repair(vertex * 2 + 2)
    self._array[vertex] = min(self._array[vertex * 2 + 1], self._array[vertex * 2 + 2])

  def _set(self, index, value, vertex, left, right):
    if left == right:
      self._array[vertex] = value
      return

    mid = (left + right) // 2
    if index <= mid:
      self._set(index, value, vertex * 2 + 1, left, mid)
    else:
      self._set(index, value, vertex * 2 + 2, mid + 1, right)

    self._array[vertex] = min(self._array[vertex * 2 + 1], self._array[vertex * 2 + 2])

  def set(self, index, value):
    self._set(index, value, 0, 0, self._size - 1)

  def _min(self, a, b, vertex, left, right):
    if b < left or a > right:
      return float("+inf")
    if a <= left and b >= right:
      return self._array[vertex]

    mid = (left + right) // 2
    l = self._min(a, b, vertex * 2 + 1, left, mid)
    r = self._min(a, b, vertex * 2 + 2, mid + 1, right)
    return min(l, r)

  def min(self, a, b):
    return self._min(a, b, 0, 0, self._size - 1)

if __name__ == "__main__":
  n, m = map(int, input().split(" "))
  array = list(map(int, input().split(" ")))

  segtree = SegmentTree.build(array)

  for _ in range(m):
    op, arg1, arg2 = map(int, input().split(" "))
    if op == 1:
      segtree.set(arg1, arg2)
    else:
      print(segtree.min(arg1, arg2 - 1))

