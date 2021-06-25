#!/usr/bin/env python3
#
# Rozszerzamy zbiór wierzchołków. Do każdego wierzchołka dodajemy informację z jaką ilością paliwa
# do niego wjechaliśmy.
#

from queue import PriorityQueue

def print_path(P, v, d, s):
  if v == s:
    return [v]
  print(v, d)
  u, d = P[v][d]
  return print_path(P, u, d, s) + [v]

def jak_dojade(G, K, d, s, t):
  n = len(G)
  D = [None] * n
  P = [None] * n
  V = [None] * n

  for i in range(n):
    D[i] = [float("+inf")] * (d + 1)
    P[i] = [-1] * (d + 1)
    V[i] = [False] * (d + 1)

  Q = PriorityQueue()

  D[s][d] = 0
  Q.put((0, (s, d)))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    _, u = Q.get()
    u, dis = u

    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u][dis]:
      continue

    V[u][dis] = True

    for v, w in enumerate(G[u]):
      if w == -1 or w > dis:
        continue

      new = dis - w
      if v in K:
        new = d

      if D[v][new] > D[u][dis] + w:
        D[v][new] = D[u][dis] + w
        P[v][new] = (u, dis)

        Q.put((D[v][new], (v, new)))

  c = min(D[t])
  if c == float("+inf"):
    return
  d = D[t].index(c)
  return print_path(P, t, d, s)

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]

P = [0,1,3]

print(jak_dojade(G, P, 5, 0, 2))
#runtests(jak_dojade)

