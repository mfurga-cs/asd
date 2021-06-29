#!/usr/bin/env python3

from collections import deque

def bfs(G, s):
  n = len(G)
  V = [False] * n
  P = [None] * n
  D = [float("+inf")] * n
  Q = deque()

  V[s] = True
  D[s] = 0
  Q.append(s)

  while len(Q) > 0:
    u = Q.popleft()

    print(u)

    for v in G[u]:
      if not V[v]:
        V[v] = True
        P[v] = u
        D[v] = D[u] + 1
        Q.append(v)

  return D


G = [
  [1, 4],
  [0, 2],
  [1, 3],
  [2, 4],
  [0, 3]
]

bfs2(G, 0)

