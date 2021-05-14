#!/usr/bin/env python3
#
# Zad. 2. Proszę podać jak najszybszy algorytm, który znajduje w grafie
# cykl długości dokładnie 4 (trywialny algorytm ma złożoność O(n^4), gdzie
# n to liczba wierzchołków---chodzi o rozwiązanie szybsze).
#

from collections import deque

def bfs(G, v):
  visited = [False] * len(G)
  dist = [-1] * len(G)
  count = [-1] * len(G)

  visited[v] = True
  dist[v] = 0

  q = deque()
  q.append(v)

  while len(q) > 0:
    u = q.popleft()

    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        q.append(v)

        dist[v] = dist[u] + 1
        count[v] = 1
      elif dist[u] + 1 == dist[v] and dist[v] == 2:
        count[v] += 1
        return True

  print(list(range(len(G))))
  print(dist)
  print(count)
  return False

def sol(G):
  bfs(G, 0)


G = [
  [1, 2],
  [0, 2, 3],
  [0, 1, 3],
  [1, 2]
]

sol(G)

