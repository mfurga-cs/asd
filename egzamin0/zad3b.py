#!/usr/bin/env python3
#
# Złożoność: O(V^3) gdzie V to liczba nowo powstałych wierzchołków tj. 2 * V.

from zad3testy import runtests
from utils import g_convert

def queue_min(Q, D):
  n = len(Q)
  m = len(Q[0])
  value = float("+inf")
  a, b = -1, -1
  for i in range(n):
    for j in range(m):
      if Q[i][j] and D[i][j] < value:
        value = D[i][j]
        a, b = i, j
  return (a, b)

def queue_empty(Q):
  n = len(Q)
  m = len(Q[0])
  for i in range(n):
    for j in range(m):
      if Q[i][j] == True:
        return False
  return True

def dijkstra(G, s):
  n = len(G)

  D = [float("+inf")] * n
  P = [None] * n
  Q = [None] * n

  for i in range(n):
    D[i] = [float("+inf")] * 2
    Q[i] = [True] * 2

  D[s][0] = 0

  while not queue_empty(Q):
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    u, t = queue_min(Q, D)
    Q[u][t] = False

    # Nie skaczemy.
    for v, w in enumerate(G[u]):
      if w == 0:
        continue
      if D[v][0] > D[u][t] + w:
        D[v][0] = D[u][t] + w

    # Skaczemy jeśli możemy.
    if t == 1:
      continue

    for v, w in enumerate(G[u]):
      if w == 0:
        continue
      for z, w in enumerate(G[v]):
        if w == 0:
          continue
        if D[z][1] > D[u][t] + max(G[u][v], G[v][z]):
          D[z][1] = D[u][t] + max(G[u][v], G[v][z])

  return D

def jumper(G, s, w):
  D = dijkstra(G, s)
  return min(D[w][0], D[w][1])

runtests(jumper)

