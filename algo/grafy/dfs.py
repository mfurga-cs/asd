#!/usr/bin/env python3

time = 0

def dfs_visit(G, u, visited, parent):
  global time

  # Start time
  visited[u] = True

  #time += 1
  #started[u] = time

  for v in G[u]:
    if not visited[v]:
      parent[v] = u
      dfs_visit(G, v, visited, parent)

  # Finish time
  #time += 1
  #finished[u] = time

def dfs(G):
  n = len(G)
  visited = [False] * n
  parent = [-1] * n

  for u in range(n):
    if not visited[u]:
      dfs_visit(G, u, visited, parent)

  return parent

G = [
  [1, 2],
  [],
  []
]

dfs(G)

