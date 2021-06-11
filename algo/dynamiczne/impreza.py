#!/usr/bin/env python3
#
# g(v) - maksymalna impreza w podrzewie zakorzenionym w v taka że nie idzie v.
#
# f(v) - maksymalne impreza w podrzewie zakorzenionym w v.
#
# g(v) = sum{ f(v) }
# f(v) = max( v.fun + sum{ g(u) }, g(v) }

class Node(object):
  def __init__(self, fun):
    self.children = []
    self.f = None
    self.g = None
    self.fun = fun

  def __repr__(self):
    return "f=%s g=%s used=%s" % (self.f, self.g, self.used)

  def add_child(self, child):
    self.children.append(child)

def g(v):
  if v.g is not None:
    return v.g
  v.g = 0
  for u in v.children:
    v.g += f(u)
  return v.g

def f(v):
  if v.f is not None:
    return v.f
  v.f = g(v)
  s = v.fun
  for u in v.children:
    s += g(u)
  v.f = max(v.f, s)
  return v.f

if __name__ == "__main__":
  root = Node(10)
  v1 = Node(10)
  v2 = Node(9)
  v3 = Node(1)

  root.add_child(v1)
  root.add_child(v2)
  root.add_child(v3)

  v4 = Node(12)
  v5 = Node(3)
  v6 = Node(7)
  v7 = Node(7)
  v8 = Node(9)
  v9 = Node(3)

  v1.add_child(v4)
  v1.add_child(v5)
  v1.add_child(v6)

  v3.add_child(v7)
  v3.add_child(v8)
  v3.add_child(v9)

  print(f(root))
  print("-----")


