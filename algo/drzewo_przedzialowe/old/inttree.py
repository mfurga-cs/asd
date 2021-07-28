#!/usr/bin/env python3
#
# Implementacja drzewa przedziałowego.
#

class InttreeNode:
  def __init__(self):
    # Standardowe pola
    self.cut = None
    self.left = None
    self.right = None
    self.lchild = None
    self.rchild = None
    self.leaf = None
    # Dodadkowe
    self.value = 0

class Inttree:
  def __init__(self, A):
    self._root = self._build_tree(A, 0, len(A) - 1, min(A), max(A))

  def _build_tree(self, A, i, j, left, right):
    node = InttreeNode()
    node.left = left
    node.right = right
    if j < i:
      # Node odpowiedzialny jest za przedział bazowy.
      node.cut = -1
      node.leaf = True
    else:
      # Node odpowiedzialny jest za sumę przedziałów zbiorowych.
      m = (i + j) // 2
      node.cut = A[m]
      node.leaf = False
      node.lchild = self._build_tree(A, i, m - 1, left, A[m])
      node.rchild = self._build_tree(A, m + 1, j, A[m], right)
    return node

  def _update(self, node, interval, value):
    (a, b) = interval

    if node is None or a >= node.right or b <= node.left:
      return

    # Sprawdzamy czy pytany przedział zawiera się w przedziale za który odpowiada node.
    if a >= node.left and b <= node.right:
      node.value = value
      # TODO: Lazy update.
      if node.leaf:
        return

    self._update(node.lchild, interval, value)
    self._update(node.rchild, interval, value)
    node.value = max(node.lchild.value, node.rchild.value)

  def update(self, interval, value):
    return self._update(self._root, interval, value)

  def _max(self, node, interval):
    (a, b) = interval

    if a >= node.right or b <= node.left:
      return 0

    if a >= node.left and b <= node.right:
      return node.value

    left = self._max(node.lchild, interval)
    right = self._max(node.rchild, interval)
    return max(left, right)

  def max(self, interval):
    return self._max(self._root, interval)


