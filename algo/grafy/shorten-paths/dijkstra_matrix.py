#!/usr/bin/env python3
# Alg. Dijkstry dla reprezentacji macierzowej.
# Złożoność: O(V^2)

from utils import g_convert

def queue_min(Q, D):
  n = len(Q)
  value = float("+inf")
  u = -1
  for v in range(n):
    if Q[v] and D[v] < value:
      value = D[v]
      u = v
  return u

def queue_empty(Q):
  n = len(Q)
  for v in range(n):
    if Q[v] == True:
      return False
  return True

def dijkstra(G, s):
  n = len(G)
  D = [float("+inf")] * n
  P = [None] * n
  Q = [False] * n

  Q[s] = True
  D[s] = 0

  while not queue_empty(Q):
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    u = queue_min(Q, D)
    Q[u] = False

    for v, w in enumerate(G[u]):
      if w == 0:
        continue
      if D[v] > D[u] + w:
        D[v] = D[u] + w
        P[v] = u
        Q[v] = True

  return D

G = """
0
1
2
3
4
#
0 1 10
1 2  1
2 3 3
2 0 4
0 4 100
3 4 20
"""
G = g_convert(G, matrix=True)
print(dijkstra(G, 0))

