#!/usr/bin/env python3

def transitive_closure(G):
  n = len(G)
  D = [row[:] for row in G]
  H = [row[:] for row in G]

  for u in range(n):
    for v in range(n):
      if u != v and G[u][v] == 0:
        D[u][v] = float("+inf")

  for k in range(n):
    for u in range(n):
      for v in range(n):
        D[u][v] = min(D[u][v], D[u][k] + D[k][v])

  for u in range(n):
    for v in range(n):
      H[u][v] = 1 if D[u][v] != float("+inf") and u != v else 0

  return H

G = [
  [0, 0, 0, 0],
  [0, 0, 1, 1],
  [0, 1, 0, 0],
  [1, 0, 0, 0]
]

transitive_closure(G)

