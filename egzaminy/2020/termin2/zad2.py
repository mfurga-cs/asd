#!/usr/bin/env python3

from zad2testy import runtests
from math import ceil

class Node(object):
  def __init__(self, value):
    self.value = value
    self.parent = self
    self.rank = 0

def find(x):
  if x != x.parent:
    x.parent = find(x.parent)
  return x.parent

def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1

def kruskal(D, n, i):
  V = [Node(i) for i in range(n)]
  c = 0
  last = 0

  for x, y, w in D[i:]:
    if find(V[x]) != find(V[y]):
      union(V[x], V[y])
      last = w
      c += 1

  return (last - D[i][2]) if c == n - 1 else float("+inf")

def highway(A):
  n = len(A)
  D = []

  for x in range(n):
    for y in range(n):
      D.append((x, y, ((A[x][0] - A[y][0]) ** 2 + (A[x][1] - A[y][1]) ** 2) ** (1/2.)))

  D = sorted(D, key=lambda x: x[2])

  m = float("+inf")
  for i in range(len(D)):
    v = kruskal(D, n, i)
    m = min(m, v)

  return ceil(m)

runtests(highway)

