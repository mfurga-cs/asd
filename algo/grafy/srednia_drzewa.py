#!/usr/bin/env python3
# Średnica w ważonym drzewie nieskierowanym reprezentowany jako macierz sąsiedztwa.
# Działa dla drzew nieważonych pod warunkiem że 1 oznacza krawędź z u do v.
# (0 zonacza brak krawędzi z wierzchołka u do v)
#
# Złożoność: O(V + E) = O(V) bo E = V - 1

from collections import deque
from utils import g_convert

# Szukamy wierzchołka, który jest najdalej położony od wierzchołka s.
def bfs(G, s):
  n = len(G)
  visited = [False] * n
  parent = [-1] * n
  distance = [0] * n

  max_vertex = -1
  max_length = float("-inf")

  queue = deque()
  visited[s] = True
  distance[s] = 0

  queue.append(s)
  while len(queue) > 0:
    u = queue.popleft()

    if distance[u] > max_length:
      max_length = distance[u]
      max_vertex = u

    for v, w in enumerate(G[u]):
      if w == 0:
        continue

      if not visited[v]:
        visited[v] = True
        parent[v] = u
        distance[v] = distance[u] + w
        queue.append(v)

  return max_length, max_vertex, parent

def diameter(G):
  _, max_vertex, _ = bfs(G, 0)
  length, v, parent = bfs(G, max_vertex)
  diam = []
  while v != -1:
    diam.append(v)
    v = parent[v]
  return diam, length

G = """
0
1
2
3
#
0 1 10
1 2 -10
1 3 1
"""
print(diameter(g_convert(G, True)))

