#!/usr/bin/env python3

from queue import PriorityQueue

def print_path(P, v, s, t):
  if v == s:
    if t == 0:
      s = "Alicja"
    if t == 1:
      s = "Bob"
    return [s, v]
  u, t = P[v][t], 1 - t
  return print_path(P, u, s, t) + [v]

def dijkstra(G, s, dest):
  n = len(G)
  D = [None] * n
  P = [None] * n
  V = [None] * n

  for i in range(n):
    D[i] = [float("+inf")] * 2
    P[i] = [-1] * 2
    V[i] = [False] * 2

  Q = PriorityQueue()

  D[s][0] = 0
  D[s][1] = 0

  # 0 - zaczyna z wierzchołka Alicja, 1 - zaczyna z wierzchołka Bob
  Q.put((0, (s, 0)))
  Q.put((0, (s, 1)))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    _, u = Q.get()
    u, t = u
    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u][t]:
      continue

    V[u][t] = True

    for v, w in G[u]:

      dist = D[u][t] + w
      if t == 1:
        # Jeżeli prowadzi Bob to nie dodajemy kosztu przejechania. (Zliczamy tylko dla Alicji)
        dist = D[u][t]

      if D[v][1 - t] > dist:
        D[v][1 - t] = dist
        P[v][1 - t] = u
        Q.put((D[v][1 - t], (v, 1 - t)))

  d = min(D[dest])
  print(d)
  i = D[dest].index(d)
  print(print_path(P, dest, s, i))

G = [
  [(1, 11), (3, 10)],
  [(0, 11), (2, 12), (3, 2)],
  [(1, 12), (3, 20)],
  [(0, 10), (2, 20), (1, 2)]
]
dijkstra(G, 0, 2)

