from zad1testy import runtests

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

  return diam, length

def best_root(L):
  diam, length = diameter(L)
  return diam[length // 2]

runtests(best_root)

