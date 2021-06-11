#!/usr/bin/env python3

def bellman_ford(G, s):
  n = len(G)
  d = [float("+inf")] * len(G)
  p = [-1] * len(G)

  d[s] = 0
  for _ in range(n):
    for u in range(n):
      for v, w in G[u]:
        if d[v] > d[u] + w:
          d[v] = d[u] + w
          p[v] = u

  print(d)

  # Check for negative cycle.
  for u in range(n):
    for v, w in G[u]:
      if d[v] > d[u] + w:
        return False
  return True



G = [
  [(2, 1), (3, 1)],       # 0
  [(3, 1), (4, 1)],       # 1
  [(3, 1), (4, 1)],       # 2
  [(0, 1)],          # 3
  [(1, 1)]           # 4
]

print(bellman_ford(G, 0))

