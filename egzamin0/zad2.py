#
#
#
from zad2testy import runtests

class Node:
  def __init__(self):
    self.left = None
    self.leftval = 0
    self.right = None
    self.rightval = 0
    self.X = None

def f(v, k):
  if v.X[k] is not None:
    return v.X[k]

  if v.left is None and v.right is None:
    if k > 0:
      return float("-inf")
    return 0

  if k == 0:
    return 0

  left_only = float("-inf")
  if v.left is not None:
    left_only = f(v.left, k - 1) + v.leftval

  right_only = float("-inf")
  if v.right is not None:
    right_only = f(v.right, k - 1) + v.rightval

  both = float("-inf")
  if v.left is not None and v.right is not None:
    for i in range(0, k - 1):
      both = max(both, f(v.left, i) + f(v.right, k - 2 - i) + v.leftval + v.rightval)

  v.X[k] = max(both, left_only, right_only)
  return v.X[k]

def init(T, k):
  if T is None:
    return
  if T.X is None:
    T.X = [None] * (k + 1)
  init(T.left, k)
  init(T.right, k)

def result(T, k):
  if T is None:
    return float("-inf")
  return max(f(T, k), result(T.left, k), result(T.right, k))

def valuableTree(T, k):
  init(T, k)
  return result(T, k)

runtests(valuableTree)

