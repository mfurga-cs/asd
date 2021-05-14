#!/usr/bin/env python3
#
# Zad. 1. Dany jest spójny graf nieskierowany G = (V,E). Proszę
# zaproponować algorytm, który znajdzie taką kolejność usuwania
# wierzchołków, która powoduje że w trakcie usuwania graf nigdy nie
# przestaje być spójny (usunięcie wierzchołka usuwa, oczywiście, wszystkie
# dotykające go krawędzie).
#

time = 0

def dfs_visit(G, u, visited, finished):
  global time

  visited[u] = True

  for v in G[u]:
    if not visited[v]:
      dfs_visit(G, v, visited, finished)

  finished[time] = u
  time += 1

def dfs(G):
  visited = [False] * len(G)
  finished = [-1] * len(G)
  dfs_visit(G, 0, visited, finished)
  print(finished)

G = [
  [1, 2],
  [0, 2, 3],
  [0, 1],
  [1, 4, 7],
  [3, 5],
  [4, 6],
  [5, 7],
  [3, 6, 8],
  [7]
]

G = [
  [1, 4],
  [0, 2, 3],
  [1],
  [1],
  [0, 5],
  [4]
]

dfs(G)

