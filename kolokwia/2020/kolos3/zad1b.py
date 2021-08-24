#!/usr/bin/env python3

from inttree import *

class TreeNode:
  def __init__(self, left=None, right=None):
    self.left = left
    self.right = right
    self.lchild = None
    self.rchild = None

    self.prefix = 0
    self.suffix = 0
    self.sum = 0
    self.lazy = False

  def __repr__(self):
    return f"[{self.left}, {self.right}] ({self.sum}, {self.prefix}, {self.suffix})"

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

def tree_print(tree, space=0):
  if tree is None:
    return

  space += 20
  tree_print(tree.rchild, space)

  for i in range(20, space):
    print(" ", end="")
  print(tree)

  tree_print(tree.lchild, space)

def tree_lazy_propagation(tree):
  if tree.lazy:
    tree.lchild.sum = tree.lchild.right - tree.lchild.left
    tree.lchild.prefix = tree.lchild.right - tree.lchild.left
    tree.lchild.suffix = tree.lchild.right - tree.lchild.left
    tree.lchild.lazy = True

    tree.rchild.sum = tree.rchild.right - tree.rchild.left
    tree.rchild.prefix = tree.rchild.right - tree.rchild.left
    tree.rchild.suffix = tree.rchild.right - tree.rchild.left
    tree.rchild.lazy = True

    tree.lazy = False

def tree_update(tree, a, b):
  if tree.right <= a or tree.left >= b:
    return

  if tree.left >= a and tree.right <= b:
    tree.sum = (tree.right - tree.left)
    tree.prefix = (tree.right - tree.left)
    tree.suffix = (tree.right - tree.left)
    tree.lazy = True
    return

  tree_lazy_propagation(tree)

  tree_update(tree.lchild, a, b)
  tree_update(tree.rchild, a, b)

  tree.sum = max(tree.lchild.sum, tree.rchild.sum, tree.lchild.suffix + tree.rchild.prefix)
  tree.prefix = tree.lchild.prefix
  if tree.lchild.sum == tree.lchild.right - tree.lchild.left:
    tree.prefix = max(tree.prefix, tree.lchild.sum + tree.rchild.prefix)

  tree.suffix = tree.rchild.suffix
  if tree.rchild.sum == tree.rchild.right - tree.rchild.left:
    tree.suffix = max(tree.suffix, tree.rchild.sum + tree.lchild.suffix)

"""
def tree_query(tree, a, b):
  if tree.right <= a or tree.left >= b:
    return float("-inf")

  if tree.left >= a and tree.right <= b:
    return tree.sum

  tree_lazy_propagation(tree)

  left = tree_query(tree.lchild, a, b)
  right = tree_query(tree.rchild, a, b)
  return max(left, right)
"""

def intervals(I):
  A = []
  for interval in I:
    A.append(interval[0])
    A.append(interval[1])
  A = sorted(A)

  i = 0; j = 0
  while j < len(A):
    while j + 1 < len(A) and A[j] == A[j + 1]:
      j += 1
    A[i] = A[j]
    i += 1
    j += 1
  A = A[:i]

  T = tree_build(A)

  result = []
  for interval in I:
    a, b = interval
    tree_update(T, a, b)
    result.append(T.sum)

  return result

run_tests(intervals)


