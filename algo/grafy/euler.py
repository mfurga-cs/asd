#!/usr/bin/env python3

from utils import g_convert

def euler(G):
  n = len(G)
  visited = [[False] * n for _ in range(n)]
  cycle = []

  def dfs_visit(u):
    for v in range(n):
      if G[u][v] == 1 and not visited[u][v]:
        visited[u][v] = True
        visited[v][u] = True
        dfs_visit(v)
    cycle.append(u)

  dfs_visit(0)
  return cycle

G = """
0
1
2
3
#
0 1
1 2
0 3
2 3
3 1
"""
G = g_convert(G, matrix=True)
print(euler(G))

