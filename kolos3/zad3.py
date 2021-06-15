from zad3testy import runtests
from zad3EK    import edmonds_karp
from queue import PriorityQueue
import copy
#
# Liczymy odlegości od każdego wierzchołka zielonego do każdego wierzchołka czerwonego.
# Tworzmy krawędzie nieskierowane o wadze 1 jeśli odlegość od 2 w parze jest większa od niż D.
# Powstały graf jest grafem dwudzileny (nie może być krawędzi do wierzchołków w tym samym kolorze).
# Szukamy maksymalengo skojarzenia tworząc 2 sztuczne wierzchołki s i t z wagami 1 i podpinamy je
# do wierzchołków zielonych i niebieskich. Maksymalne skojarzenie znajdujemy przy pomocy maxflow.
#

def dijkstra(G, s, t):
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

    if u == t:
      return D[u]

    for v, w in enumerate(G[u]):
      if w == 0:
        continue
      if D[v] > D[u] + w:
        D[v] = D[u] + w
        P[v] = u
        Q.put((D[v], v))

def BlueAndGreen(T, K, D):
  n = len(T)
  H = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

  blues = []
  greens = []

  for i in range(len(K)):
    if K[i] == "B":
      blues.append(i)
    else:
      greens.append(i)

  for s in blues:
    for t in greens:
      d = dijkstra(T, s, t)
      if d >= D:
        H[s][t] = 1
        H[t][s] = 1

  # Łączymy wierzchołek n z niebieskimi.
  for i in blues:
    H[n][i] = 1
    H[i][n] = 1

  # Łączymy wierzchołek (n + 1) z zielonymi.
  for i in greens:
    H[n + 1][i] = 1
    H[i][n + 1] = 1

  return edmonds_karp(H, n, n + 1)

runtests( BlueAndGreen )

