#
# Rozmnażamy wierzchołki. Do każdego dodajemy informację czy użyliśmy dwumilowych butów.
#

from zad3testy import runtests
from queue import PriorityQueue

def dijkstra(G, s):
  n = len(G)

  D = [float("+inf")] * n
  P = [None] * n
  V = [False] * n

  for i in range(n):
    D[i] = [float("+inf")] * 2
    V[i] = [False] * 2

  Q = PriorityQueue()

  D[s][0] = 0
  D[s][1] = 0
  Q.put((0, (s, 0)))

  while Q.qsize() > 0:
    # Zdejmowany wierzchołek z kolejki ma prawidłowo przypisaną najktótszą odległość D[u] do s.
    _, u = Q.get()
    (u, t) = u
    # Musimy pominąć wierzchołki, które włożyliśmy z większą wagą a które były już przetowrzone.
    if V[u][t]:
      continue
    V[u][t] = True

    # Nie skarzemy.
    for v, w in enumerate(G[u]):
      if w == 0:
        continue
      if D[v][0] > D[u][t] + w:
        D[v][0] = D[u][t] + w
        Q.put((D[v][0], (v, 0)))

    if t == 1:
      continue

    # Skaczemy o 2 wierzchołki dalej.
    for v, w in enumerate(G[u]):
      if w == 0:
        continue

      for z, w in enumerate(G[v]):
        if w == 0:
          continue

        if D[z][1] > D[u][t] + max(G[u][v], G[v][z]):
          D[z][1] = D[u][t] + max(G[u][v], G[v][z])
          Q.put((D[z][1], (z, 1)))

  return D

def jumper(G, s, w):
  D = dijkstra(G, s)
  return min(D[w][0], D[w][1])

runtests(jumper)

