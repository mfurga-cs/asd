from zad1testy import runtests
#
# Liczymy odleglości dla wszystkich wierzchołków w grafie przy użyciu alg. Floyda-Warshalla.
# Rozmnażamy wierzchołki do każdego dodajemy informację w jakim wierzchołku jest druga osoba.
# Każdy wierzchołek reprezentujemy jako parę (u, v) gdzie u oznacza pozycję Carola
# (oryginaly wierzchołek w grafie) a v pozycję Maxa. Niektóre z nich nie będą mogły istnieć
# ponieważ odlegość pomiędzy (u, v) w oryginalym grafie może być < d. Tworzymy krawędzie
# w nowym grafie pomiędzy wierzchołkami (u, v) i (x, y) wtedy gdy pomiędzy wierzchołkiem
# oryginalnym u jest krawędz do x oraz jeśli z v jest do y. Jeśli dana osoba się nie porusza
# wtedy odpowiedni wierzchołek pozostaje bez zmiany a drugi się zmienia.
# Teraz wystarczy znaleźć scieżkę pomiędzy x i y.
#

def floyd_warshall(G):
  n = len(G)
  D = [row[:] for row in G]

  for u in range(n):
    for v in range(n):
      if u != v and G[u][v] == 0:
        D[u][v] = float("+inf")

  for k in range(n):
    for u in range(n):
      for v in range(n):
        if D[u][v] > D[u][k] + D[k][v]:
          D[u][v] = D[u][k] + D[k][v]

  return D

def dfs_visit(G, D, d, u, v, visited, parent):
  visited[u][v] = True

  for uu, w in enumerate(G[u]):
    if w == 0:
      continue

    for vv, w in enumerate(G[v]):
      if w == 0:
        continue

      if D[uu][vv] == float("+inf") or D[uu][vv] < d or (v == uu and vv == u):
        continue

      if not visited[uu][vv]:
        parent[uu][vv] = (u, v)
        dfs_visit(G, D, d, uu, vv, visited, parent)

  # 2 przypadki dla których nie zmieniamy jednego wierzchołka.
  for vv, w in enumerate(G[v]):
    if w == 0:
      continue

    if D[u][vv] == float("+inf") or D[u][vv] < d:
      continue

    if not visited[u][vv]:
      parent[u][vv] = (u, v)
      dfs_visit(G, D, d, u, vv, visited, parent)

  for uu, w in enumerate(G[u]):
    if w == 0:
      continue

    if D[uu][v] == float("+inf") or D[uu][v] < d:
      continue

    if not visited[uu][v]:
      parent[uu][v] = (u, v)
      dfs_visit(G, D, d, uu, v, visited, parent)

def dfs(G, D, d, x, y):
  n = len(G)

  visited = [False] * n
  for i in range(n):
    visited[i] = [False] * n

  parent = [None] * len(G)
  for i in range(n):
    parent[i] = [None] * n

  dfs_visit(G, D, d, x, y, visited, parent)

#  print("====== parent")
#  for row in parent:
#    print(row)

#  print("====== visited")
#  for row in visited:
#    print(row)

  return get_solution(parent, y, x)


def get_solution(P, u, v):
  if P[u][v] is None:
    return [(u, v)]
  a, b = P[u][v]
  return get_solution(P, a, b) + [(u, v)]
"""
def dfs_visit(G, u, v, visited, parent):
  visited[u][v] = True

  for uu, vv in G[u][v]:
    if not visited[uu][vv]:
      parent[uu][vv] = (u, v)
      dfs_visit(G, uu, vv, visited, parent)

def dfs(G, x, y):
  n = len(G)
  visited = [False] * n
  parent = [None] * n

  for i in range(n):
    visited[i] = [False] * n
    parent[i] = [None] * n

  dfs_visit(G, x, y, visited, parent)
  return get_solution(parent, y, x)

def build_G(G, M, D, d, u, v):
  n = len(M)

  for uu in range(n):
    for vv in range(n):
      if (M[u][uu] != 0 or u == uu) and (M[v][vv] != 0 or v == vv) and (not (v == uu and u == vv)) and D[uu][vv] >= d:
        G[u][v].append((uu, vv))

"""

def keep_distance(M, x, y, d):
  n = len(M)

  D = floyd_warshall(M)
#  G = [[[] for v in range(n)] for u in range(n)]

#  for u in range(n):
#    for v in range(n):
#      build_G(G, M, D, d, u, v)

  return dfs(M, D, d, x, y)


M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2

#print(keep_distance(M, x, y, d))

runtests(keep_distance)

