#!/usr/bin/env python3

def dfs_visit(G, u, visited):
  for v in range(len(G[u])):
    if G[u][v] == 1:
      G[u][v] = 0
      G[v][u] = 0
      dfs_visit(G, v, visited)
  visited.append(u)

def euler(G):
  visited = []
  dfs_visit(G, 0, visited)
  print(visited)

G = [
  [0, 1, 0, 0, 0, 1],  # 0
  [1, 0, 1, 0, 1, 1],  # 1
  [0, 1, 0, 1, 1, 1],  # 2
  [0, 0, 1, 0, 1, 0],  # 3
  [0, 1, 1, 1, 0, 1],  # 4
  [1, 1, 1, 0, 1, 0]   # 5
]

euler(G)

