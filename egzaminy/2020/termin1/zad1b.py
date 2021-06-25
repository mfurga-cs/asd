#!/usr/bin/env python3
#
# Złożoność: O(V^2), gdzie V to liczba nowo postałych wierzchołków (tj. 3 * V).
#

from zad1testy import runtests

def weight(t):
  if t == 0:
    return 1
  if t == 2:
    return 5
  if t == 2:
    return 8
  return None

def type(w):
  if w == 1:
    return 0
  if w == 5:
    return 1
  if w == 8:
    return 2
  return None

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

def dijkstra(G, s, k):
  n = len(G)

  D = [float("+inf")] * n
  Q = [None] * n

  for i in range(n):
    D[i] = [float("+inf")] * 3
    Q[i] = [False] * 3

  for i in range(3):
    D[s][i] = 0
    Q[s][i] = True

  while not queue_empty(Q):
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    u, t = queue_min(Q, D)
    Q[u][t] = False

    for v, w in enumerate(G[u]):
      if w == 0:
        continue

      if weight(t) == w:
        continue

      if D[v][type(w)] > D[u][t] + w:
        D[v][type(w)] = D[u][t] + w
        Q[v][type(w)] = True

  return min(D[k][0], D[k][1], D[k][2])

runtests(dijkstra)

