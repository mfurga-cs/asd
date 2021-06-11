#!/usr/bin/env python3

SPACE_GAP = 5

def print_bst(bst):
  _print_bst(bst.root, 0)

def _print_bst(root, space):
  if root == None:
    return
  space += SPACE_GAP

  _print_bst(root.right, space)
  print()
  for i in range(SPACE_GAP, space):
    print(end=" ")
  print(root.value)
  _print_bst(root.left, space)




class BSTNode(object):
  def __init__(self, value, parent, left, right):
    self.value = value
    self.parent = parent
    self.left = left
    self.right = right

class BST(object):
  def __init__(self):
    self.root = None

  def find(self, value):
    curr = self.root
    while curr is not None:
      if curr.value == value:
        return curr
      if curr.value > value:
        curr = curr.left
      else:
        curr = curr.right
    return None

  def maximum(self, node):
    while node.right is not None:
      node = node.right
    return node

  def minimum(self, node):
    while node.left is not None:
      node = node.left
    return node

  def insert(self, value):
    if self.root is None:
      self.root = BSTNode(value, None, None, None)
      return

    prev = None
    curr = self.root
    while curr is not None:
      prev = curr
      if curr.value >= value:
        curr = curr.left
      else:
        curr = curr.right

    node = BSTNode(value, prev, None, None)
    if prev.value >= value:
      prev.left = node
    else:
      prev.right = node

  def successor(self, value):
    x = self.find(value)
    if x is None:
      return None

    if x.right is not None:
      return self.minimum(x.right)

    y = x.parent
    while y is not None and x == y.right:
      x = y
      y = y.parent
    return y

  def predecessor(self, value):
    x = self.find(value)
    if x is None:
      return None

    if x.left is not None:
      return self.maximum(x.left)

    y = x.parent
    while y is not None and x == y.left:
      x = y
      y = y.parent
    return y

if __name__ == "__main__":
  bst = BST()
  bst.insert(5)
  bst.insert(2)
  bst.insert(9)
  bst.insert(0)
  bst.insert(4)
  bst.insert(7)
  bst.insert(6)
  print_bst(bst)

  v = bst.predecessor(6)
  print(v.value)


