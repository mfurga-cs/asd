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
    self.lazy = None

  def __repr__(self):
    return f"[{self.left}, {self.right}]"

def _tree_build(points, left, right):
  node = TreeNode(points[left], points[right])
  if left + 1 == right:
    return node
  mid = (left + right) // 2
  node.lchild = _tree_build(points, left, mid)
  node.rchild = _tree_build(points, mid, right)
  return node

def tree_build(points):
  return _tree_build(points, 0, len(points) - 1)

def tree_lazy_propagation(tree):
  if tree.lazy is not None:
    tree.lchild.max = tree.lazy
    tree.lchild.lazy = tree.lazy
    tree.rchild.max = tree.lazy
    tree.rchild.lazy = tree.lazy
    tree.lazy = None

def tree_update(tree, a, b, value):
  if tree.right <= a or tree.left >= b:
    return

  if tree.left >= a and tree.right <= b:
    tree.max = value
    tree.lazy = value
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
  points = list(map(int, input().split()))
  tree = tree_build(points)

  while line := input():
    op, a, b, value = (list(map(int, line.split())) + [None])[:4]
    if op == 1:
      tree_update(tree, a, b, value)
    else:
      v = tree_query(tree, a, b)
      print(v)


