#!/usr/bin/env python3
#
# Wyznaczamy wierzchołki, które biorą udział w najkrótszych scieżkach poprzed wykonanie
# 2 razy BFS z wierzchołka s i z wierzchołka t. Jeśli dla danego wierzchołka
# dist_s[v] + dist_t[v] == shortest_path_length to znaczy że jest on na najkrótszych ścieżkach
# z s do t. Dzielimy teraz te wierzchołki na grupy w zależności od odległości od s.
# Teraz jeśli znajdziemy 2 sąsiednie grupy które mają po jednym wierzchołu to będzie to oznaczać
# że po usunięciu tej krawędzie najkrótsza scieżka z s do t przestanie istnieć.
#
# Złożoność: O(V + E)
#

from collections import deque
from zad2testy import runtests

def bfs(G, s):
  n = len(G)
  V = [False] * n
  P = [None] * n
  D = [float("+inf")] * n
  Q = deque()

  V[s] = True
  D[s] = 0
  Q.append(s)

  while len(Q) > 0:
    u = Q.popleft()
    for v in G[u]:
      if not V[v]:
        V[v] = True
        P[v] = u
        D[v] = D[u] + 1
        Q.append(v)

  return D

def enlarge(G, s, t):
  n = len(G)
  dist_s = bfs(G, s)
  dist_t = bfs(G, t)

  shortest_path = dist_s[t]
  divisions = [[] for _ in range(shortest_path + 1)]

  for i in range(n):
    if dist_s[i] + dist_t[i] == shortest_path:
      divisions[dist_s[i]].append(i)

  result = None

  for i in range(1, shortest_path + 1):
    if len(divisions[i - 1]) == len(divisions[i]) == 1:
      result = (divisions[i - 1][0], divisions[i][0])

  return result

runtests(enlarge)

