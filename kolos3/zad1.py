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

def print_solution(P, x, y, u, v):
  if u == x and v == y:
    return []
  a, b = P[u][v]
  return print_solution(P, x, y, a, b) + [(u, v)]

def dfs_visit(G, D, d, u, v, visited, parent):
  visited[u][v] = True

  for uu, w in enumerate(G[u]):
    if w == 0:
      continue

    for vv, w in enumerate(G[v]):
      if w == 0:
        continue

      if D[uu][vv] == float("+inf") or D[uu][vv] < d:
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

  parent = [-1] * len(G)
  for i in range(n):
    parent[i] = [-1] * n

  dfs_visit(G, D, d, x, y, visited, parent)
  return print_solution(parent, x, y, y, x)

def keep_distance(M, x, y, d):
  D = floyd_warshall(M)
  return dfs(M, D, d, x, y)

runtests(keep_distance)

