#!/usr/bin/env python3

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

if __name__ == "__main__":
  bst = BST()

  assert bst.min() == None
  assert bst.max() == None
  assert bst.find(10) == None

  bst.insert(20)
  assert bst.min().value == 20
  assert bst.max().value == 20
  bst.delete(20)
  bst.delete(20)

  bst.insert(20)
  bst.insert(20)

  bst.insert(10)
  bst.insert(30)
  assert bst.min().value == 10
  assert bst.max().value == 30

  bst.insert(5)
  assert bst.find(5).value == 5
  assert bst.find(1) == None

  bst.insert(15)
  bst.insert(17)
  bst.insert(25)
  bst.insert(35)

  assert bst.min().value == 5
  assert bst.max().value == 35

  assert bst.find(17).value == 17
  bst.delete(17)
  assert bst.find(17) == None
  bst.insert(17)
  assert bst.find(17).value == 17

  assert bst.successor(5).value == 10
  assert bst.successor(10).value == 15
  assert bst.successor(20).value == 20
  assert bst.successor(35) == None
  assert bst.successor(17).value == 20
  assert bst.successor(25).value == 30

  print(bst)

  assert bst.predecessor(5) == None
  assert bst.predecessor(35).value == 30
  assert bst.predecessor(17).value == 15
  assert bst.predecessor(20).value == 17
  assert bst.predecessor(20).value == 17



