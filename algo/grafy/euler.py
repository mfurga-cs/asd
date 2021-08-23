#!/usr/bin/env python3

from utils import g_convert

# Matrix. Czas: O(V^3), pamięć: O(V^2)
# Na pewno działa ale słaba złożoność.
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

# Matrix. Czas: O(V^2), pamięć: O(V)
def euler(G):
  n = len(G)
  # pos[v] wstazuje na kolejny wierzchołek do przeszukania w wierszu sąsiedztwa
  # dla wierzchołka v. Dzięki temu gwarantujemy że przeglądanie wiersza dla danego
  # wierzchołka będzie zajmowało dokładnie O(V) czasu (zamortyzowanego) pomiędzy
  # kolejnymi wykonaniami rekurencyjnymi.
  pos = [0] * n
  cycle = []

  def dfs_visit(u):
    while pos[u] < n:
      v = pos[u]
      pos[u] += 1
      # Jeżeli pos[v] <= u lub 0 tzn krawędź v-u nie została jeszcze odwiedzona.
      if G[u][v] == 1 and (pos[v] <= u or pos[v] == 0):
        dfs_visit(v)
    cycle.append(u)

  dfs_visit(0)
  return cycle

# List. Czas: O((V + E) * V), pamięć: O(V^2)
def euler(G):
  n = len(G)
  visited = [[False] * n for _ in range(n)]
  cycle = []

  def dfs_visit(u):
    for v, _ in G[u]:
      if not visited[u][v]:
        visited[u][v] = True
        visited[v][u] = True
        dfs_visit(v)
    cycle.append(u)

  dfs_visit(0)
  return cycle

# List. Czas: O(V + E), pamięć: O(V^2)
def euler(G):
  n = len(G)
  # pos[v] wstazuje na kolejny wierzchołek do przeszukania w liście sąsiedztwa
  # dla wierzchołka v. Dzięki temu gwarantujemy że przeglądanie listy dla danego
  # wierzchołka będzie zajmowało dokładnie O(deg(v)) czasu (zamortyzowanego) pomiędzy
  # kolejnymi wykonaniami rekurencyjnymi.
  pos = [0] * n
  visited = [[False] * n for _ in range(n)]
  cycle = []

  def dfs_visit(u):
    while pos[u] < len(G[u]):
      v = G[u][pos[u]][0]  # [0] bo pary (v, w).
      pos[u] += 1
      if not visited[u][v]:
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
4
5
#
0 1
0 5
1 5
1 2
1 4
2 5
2 4
2 3
3 4
4 5
"""
G = g_convert(G, matrix=False)
print(euler(G))

