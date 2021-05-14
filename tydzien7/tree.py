#!/usr/bin/env python3

from collections import deque

def neighbors(v):
  return v

def DFS(G, s):
  V = [False] * len(G)   # Visited
  P = [-1] * len(G)      # Parent
  N = [0] * len(G)       # Number of vertixes in subtree

  def DFS_visit(u):
    V[u] = True

    i = 1
    for v in neighbors(G[u]):
      if not V[v]:
        P[v] = u
        DFS_visit(v)
        i += N[v]

    N[u] = i

  DFS_visit(s)
  print(N)

G = [
  [1, 2, 3],
  [4, 5],
  [],
  [],
  [],
  []
]

DFS(G, 0)

