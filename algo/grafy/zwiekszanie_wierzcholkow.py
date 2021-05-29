#!/usr/bin/env python3

from queue import PriorityQueue

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

def dijkstra(G, s, k):
  n = len(G)
  D = [None] * n
  P = [None] * n
  V = [None] * n

  for i in range(n):
    D[i] = [float("+inf")] * 3
    P[i] = [-1] * 3
    V[i] = [False] * 3

  Q = PriorityQueue()

  for i in range(3):
    D[s][i] = 0
    Q.put((0, (s, i)))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    _, u = Q.get()
    u, t = u

    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u][t]:
      continue

    V[u][t] = True

    for v, w in enumerate(G[u]):
      if w == 0:
        continue

      if weight(t) == w:
        continue

      if D[v][type(w)] > D[u][t] + w:
        D[v][type(w)] = D[u][t] + w
        P[v][type(w)] = u

        Q.put((D[v][type(w)], (v, type(w))))

  print(D[k][0], D[k][1], D[k][2])

G = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

dijkstra(G, 5, 2)

