#!/usr/bin/env python3

time = 0
parent = []
visited = []
low = []
d = []

def dfs_visit(G, u):
  global time

  # Start time
  visited[u] = True

  time += 1
  low[u] = d[u] = time

  for v in G[u]:
    if not visited[v]:
      parent[v] = u
      dfs_visit(G, v)
      low[u] = min(low[u], low[v])
    elif v != parent[u]:
      low[u] = min(low[u], d[v])

def dfs(G):
  global parent
  global visited
  global low
  global d

  visited = [False] * len(G)
  parent = [-1] * len(G)
  d = [-1] * len(G)
  low = [-1] * len(G)

  for u in range(len(G)):
    if not visited[u]:
      dfs_visit(G, u)

  # Wypisywanie mostów.
  for i in range(len(G)):
    if low[i] == d[i] and i != 0:
      print(parent[i], i)

G = [
  [1, 6],
  [0, 2],
  [1, 3, 6],
  [2, 4, 5],
  [3, 5],
  [3, 4],
  [0, 2, 7],
  [6],
]

G = [
  [1,2,3],
  [0,2],
  [0,1],
  [0,4],
  [3]
]

dfs(G)

