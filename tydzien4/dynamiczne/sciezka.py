#!/usr/bin/env python3

class Node(object):
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    self.f = float("-inf")

def mpath(v):
  if v is None:
    return float("-inf")
  f = v.val
  f = max(f, mpath(v.left) + v.val)
  f = max(f, mpath(v.right) + v.val)
  v.f = f
  return f

def result(v):
  if v is None:
    return float("-inf")
  m = v.f

  if v.left is not None and v.right is not None:
    m = max(m, v.left.f + v.right.f + v.val)

  return max(m, result(v.left), result(v.right))

root = Node(-4)
root.left = Node(10)
root.right = Node(-8)

child = root.left
child.left = Node(7)
child.right = Node(-5)

l = child.left
r = child.right

l.left = Node(8)
l.right = Node(-7)
l.right.right = Node(1)

r.right = Node(2)
r.right.left = Node(20)
r.right.right = Node(7)

l = l.left
l.left = Node(1)
l.left.left = Node(-5)
l.left.left.left = Node(-4)



