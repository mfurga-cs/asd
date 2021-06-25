from zad3testy import runtests

def dfs_visit(G, u, visited, top):
  visited[u] = True

  for v, w in enumerate(G[u]):
    if w == 0:
      continue
    if not visited[v]:
      dfs_visit(G, v, visited, top)

  top.append(u)

def dfs(G):
  n = len(G)
  visited = [False] * len(G)
  top = []

  for u in range(n):
    if not visited[u]:
      dfs_visit(G, u, visited, top)

  return top[::-1]

def tasks(G):
  n = len(G)
  H = [[0] * n for _ in range(n)]

  for u in range(n):
    for v in range(n):
      if G[u][v] == 1:
        H[u][v] = 1
      if G[u][v] == 2:
        H[v][u] = 1

  return dfs(H)

runtests(tasks)

