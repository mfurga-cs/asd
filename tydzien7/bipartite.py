#!/usr/bin/env python3
  # Próbujemy kolorować graf przy użyciu 2 kolorów. O(V + E).

from collections import deque

def is_bipartite(G):
  n = len(G)
  Q = deque()
  C = [False] * n

  color = 0
  C[0] = color

  Q.append(0)
  while len(Q) > 0:
    u = Q.popleft()
    color = 1 - C[u]

    for v in G[u]:
      if C[v] is False:
        C[v] = color
        Q.append(v)
      else:
        if C[v] == C[u]:
          return False

  return True

G = [
  [3],          # 0
  [3, 4],       # 1
  [3, 4],       # 2
  [0, 1, 2],    # 3
  [1, 2]        # 4
]

print(is_bipartite(G))

