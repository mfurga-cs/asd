#!/usr/bin/env python3
# Alg. Dijkstry dla reprezentacji listowej.
# Złożoność: O(ElogV)

from queue import PriorityQueue
from utils import g_convert

def dijkstra(G, s):
  n = len(G)
  D = [float("+inf")] * n
  P = [None] * n
  V = [False] * n

  Q = PriorityQueue()

  D[s] = 0
  Q.put((0, s))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    _, u = Q.get()
    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u]:
      continue
    V[u] = True

    for v, w in G[u]:
      if D[v] > D[u] + w:
        D[v] = D[u] + w
        P[v] = u
        Q.put((D[v], v))

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
print(dijkstra(g_convert(G), 0))

