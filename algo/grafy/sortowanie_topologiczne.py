#!/usr/bin/env python3
# Sortowanie topologiczne DAGu.

def dfs_visit(G, u, visited, top):
  # Start time
  visited[u] = True

  for v in G[u]:
    if not visited[v]:
      dfs_visit(G, v, visited, top)

  # Finish time
  top.append(u)

def dfs(G):
  visited = [False] * len(G)
  top = []

  for u in range(len(G)):
    if not visited[u]:
      dfs_visit(G, u, visited, top)

  # Top jako stos.
  print(top[::-1])

G = [
  [1],
  [],
  [0, 3],
  [0],
  [2, 3]
]

dfs(G)

