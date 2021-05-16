#!/usr/bin/env python3
# Diameter of a tree.

def dfs_visit(G, u, visited, parent, started):
  max_dist = started[u]
  max_vertex = u

  for v in G[u]:
    if not visited[v]:
      visited[v] = True
      parent[v] = u
      started[v] = started[u] + 1

      dist, vertex = dfs_visit(G, v, visited, parent, started)
      if dist > max_dist:
        max_dist = dist
        max_vertex = vertex

  return max_dist, max_vertex

def dfs(G, u, parent):
  visited = [False] * len(G)
  started = [-1] * len(G)
  visited[u] = True
  started[u] = 0
  return dfs_visit(G, u, visited, parent, started)

def diameter(G):
  parent = [-1] * len(G)
  _, v = dfs(G, 0, parent)

  parent = [-1] * len(G)
  length, v = dfs(G, v, parent)

  diam = []
  while v != -1:
    diam.append(v)
    v = parent[v]

  print(diam, length)

G = [ [ 2 ],
[ 2 ],
[ 0, 1, 3],
[ 2, 4 ],
[ 3, 5, 6 ],
[ 4, 7 ],
[ 4 , 8],
[5, 10],
[6, 9],
[8, 12],
[7, 11],
[10],
[9],
]

diameter(G)

