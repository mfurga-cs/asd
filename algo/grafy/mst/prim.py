#!/usr/bin/env python3

from queue import PriorityQueue

def prim(G):
  n = len(G)

  # K[v] zawiera informajcę o obecnej wadzę krawędzi lekkiej kończącej się na wierzchołku
  # v z P[v].
  K = [float("+inf")] * n
  V = [False] * n
  P = [None] * n

  Q = PriorityQueue()
  Q.put((0, 0))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki najeży do przekroju V - S i tworzy krawędź lekką z
    # wierzchołkiem P[u]. Wierzchołki, które są visited należa do budowanego przekroju S.
    _, u = Q.get()
    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u]:
      continue
    V[u] = True

    for v, w in G[u]:
      if not V[v] and w < K[v]:
        K[v] = w
        P[v] = u
        Q.put((w, v))

  # Minimalne drzewo rozpinające tworzą krawędzię (P[u], u) dla każdego wierzchołka u.

  result = []
  for i in range(1, n):
    result.append((P[i], i))
  return result

G = [
  [(1, 3), (5, 2)],
  [(0, 3), (2, 5), (5, 1)],
  [(1, 5), (3, 9)],
  [(2, 9), (4, 1), (5, 3)],
  [(3, 1), (5, 7)],
  [(0, 2), (1, 1), (3, 3), (4, 7)]
]

print(prim(G))

