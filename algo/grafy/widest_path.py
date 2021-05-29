#!/usr/bin/env python3
#
# Szukamy scieżki z wierzchołka s o maksymalnej pojemności. Tzn scieżki o największej wadzę, która
# jest najmniejsza.
#

from queue import PriorityQueue

def dijkstra(G, s):
  n = len(G)
  # Ustawiamy przpustowości każdego wierzchołka na 0.
  C = [0] * n
  P = [None] * n
  V = [False] * n

  Q = PriorityQueue()

  # W s mamy inf przepustowość.
  C[s] = float("+inf")
  Q.put((0, s))

  while Q.qsize() > 0:
    _, u = Q.get()
    if V[u]:
      continue
    V[u] = True

    for v, w in G[u]:
      # Poprawiamy przpustowość w wierzchołku v wybierając min(parenta i wagi).
      if C[v] < min(C[u], w):
        C[v] = min(C[u], w)
        P[v] = u
        # Wkładamy z wagą * -1 aby otrzymać max heap.
        Q.put((C[v] * -1, v))

  print(C[2])

G = [
  [(1, 10), (3, 5)],
  [(0, 10), (3, 10), (2, 7)],
  [(1, 7), (3, 20)],
  [(0, 5), (1, 10), (2, 20)]
]
dijkstra(G, 0)

