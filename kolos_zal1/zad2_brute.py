from zad2testy import runtests
from copy import deepcopy

def remove_vertex(G, u):
  n = len(G)
  vs = []

  for v in range(n):
    if G[u][v] == 1:
      vs.append(v)
      G[u][v] = 0

  for v in vs:
    G[v][u] = 0

  return G

def dfs_visit(G, u, visited, finished):
  visited[u] = True
  for v, w in enumerate(G[u]):
    if w == 0:
      continue
    if not visited[v]:
      dfs_visit(G, v, visited, finished)
  finished.append(u)

def scc(G):
  # Wykonujemy DFS dla grafu G.
  visited = [False] * len(G)
  finished = []

  for u in range(len(G)):
    if not visited[u]:
      dfs_visit(G, u, visited, finished)

  # Tworzymy graf T.
  T = G

  visited = [False] * len(T)
  c = 0
  for u in finished[::-1]:
    if not visited[u]:
      comp = []
      dfs_visit(T, u, visited, comp)
      c += 1
  return c

def breaking(G):
  n = len(G)
  c = scc(G)
  s = None

  for i in range(n):
    H = deepcopy(G)
    remove_vertex(H, i)
    v = scc(H) - 1
    if c < v:
      c = v
      s = i

  return s


G = [
  [0, 1, 1],
  [1, 0, 0],
  [1, 0, 0]
]



for row in G:
  print(row)

H = deepcopy(G)
remove_vertex(H, 1)

print("===== G")
for row in G:
  print(row)

print("===== H")
for row in H:
  print(row)
runtests( breaking )

