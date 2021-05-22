#!/usr/bin/env python3

class FAU:
  def __init__(self, n):
    self.P = list(range(n))
    self.R = [0] * n

  def find(self, x):
    if x != self.P[x]:
      self.P[x] = self.find(self.P[x])
    return self.P[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if self.R[x] > self.R[y]:
      self.P[y] = x
    else:
      self.P[x] = y
      if self.R[x] == self.R[y]:
        self.R[y] += 1

def edges(G):
  visited = [False] * len(G)
  E = []
  for u in range(len(G)):
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        E.append((u, v, w))
  return E

def kruskal(G):
  n = len(G)
  E = edges(G)
  E = sorted(E, key=lambda x: x[2])
  fau = FAU(n)

  result = []
  for u, v, w in E:
    if fau.find(u) != fau.find(v):
      fau.union(u, v)
      result.append((u, v, w))

  return result

G = [
  [(1, 3), (5, 2)],
  [(0, 3), (2, 5), (5, 1)],
  [(1, 5), (3, 9)],
  [(2, 9), (4, 1), (5, 3)],
  [(3, 1), (5, 7)],
  [(0, 2), (1, 1), (3, 3), (4, 7)]
]


print(kruskal(G))

