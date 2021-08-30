#!/usr/bin/env python3
#
# Implementacja drzewa przedziałowego typu przedział-przedział z max na przedziale.
# Drzewo off-line budowane z puntków bazowych końców przedziałów.
#

class TreeNode:
  def __init__(self, left=None, right=None):
    self.left = left
    self.right = right
    self.lchild = None
    self.rchild = None

    self.max = 0
    self.lazy = False

  def __repr__(self):
    return f"[{self.left}, {self.right}] {self.max} {'[+]' if self.lazy else '[-]'}"

def _tree_build(points, left, right):
  node = TreeNode(points[left], points[right])
  if left + 1 == right:
    return node
  mid = (left + right) // 2
  node.lchild = _tree_build(points, left, mid)
  node.rchild = _tree_build(points, mid, right)
  return node

def tree_build(intervals):
  points = []
  for interval in intervals:
    points.append(interval[0])
    points.append(interval[1])
  points = sorted(points)
  i = 0; j = 0
  while j < len(points):
    while j + 1 < len(points) and points[j] == points[j + 1]:
      j += 1
    points[i] = points[j]
    i += 1
    j += 1
  points = points[:i]
  return _tree_build(points, 0, len(points) - 1)

def tree_lazy_propagation(tree):
  if tree.lazy:
    tree.lchild.max = tree.max
    tree.lchild.lazy = True
    tree.rchild.max = tree.max
    tree.rchild.lazy = True
    tree.lazy = False

def tree_update(tree, a, b, value):
  if tree.right <= a or tree.left >= b:
    return

  if tree.left >= a and tree.right <= b:
    tree.max = value
    tree.lazy = True
    return

  tree_lazy_propagation(tree)

  tree_update(tree.lchild, a, b, value)
  tree_update(tree.rchild, a, b, value)

  tree.max = max(tree.lchild.max, tree.rchild.max)

def tree_query(tree, a, b):
  if tree.right <= a or tree.left >= b:
    return float("-inf")

  if tree.left >= a and tree.right <= b:
    return tree.max

  tree_lazy_propagation(tree)

  left = tree_query(tree.lchild, a, b)
  right = tree_query(tree.rchild, a, b)
  return max(left, right)

if __name__ == "__main__":
  from utils import tree_print

  blocks = [(1, 3, 1), (5, 6, 1), (2, 4, 1), (2, 7, 2)]
  intervals = [(b[0], b[1]) for b in blocks]
  tree = tree_build(intervals)
  #tree_print(tree)

  for block in blocks:
    tree_update(tree, block[0], block[1], block[2])

  tree_print(tree)
  print(tree_query(tree, 6, 7))
  tree_print(tree)


