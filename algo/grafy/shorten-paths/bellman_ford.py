#!/usr/bin/env python3
#
# Złożoność: O(VE)
#

def bellman_ford(G, s):
  d = [float("+inf")] * len(G)
  p = [-1] * len(G)

  d[s] = 0
  for _ in range(len(G)):

    for u in range(len(G)):
      for v, w in G[u]:
        if d[v] > d[u] + w:
          d[v] = d[u] + w
          p[v] = u

  print(d)

  for u in range(len(G)):
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

