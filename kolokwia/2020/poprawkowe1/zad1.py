#!/usr/bin/env python3
#
# Do każdego wierzchołka dodajemy informację z jaką ilością paliwa do niego wjechaliśmy.
#
# Złożoność: O(V^2 * d^2)
#

from zad1testy import runtests

def print_path(P, v, d, s):
  if v == s:
    return [v]
  u, d = P[v][d]
  return print_path(P, u, d, s) + [v]

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

def jak_dojade(G, K, d, s, t):
  n = len(G)
  D = [None] * n
  P = [None] * n
  Q = [None] * n
  S = [v in K for v in range(n)]

  for i in range(n):
    D[i] = [float("+inf")] * (d + 1)
    P[i] = [-1] * (d + 1)
    Q[i] = [False] * (d + 1)

  D[s][d] = 0
  Q[s][d] = True

  while not queue_empty(Q):
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    u, dis = queue_min(Q, D)
    Q[u][dis] = False

    for v, w in enumerate(G[u]):
      if w == -1 or w > dis:
        continue

      new = dis - w
      if S[v]:
        new = d

      if D[v][new] > D[u][dis] + w:
        D[v][new] = D[u][dis] + w
        P[v][new] = (u, dis)
        Q[v][new] = True

  c = min(D[t])
  if c == float("+inf"):
    return
  d = D[t].index(c)
  return print_path(P, t, d, s)

runtests(jak_dojade)

