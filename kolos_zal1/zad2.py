#!/usr/bin/env python3
# Szukamy punktów artykulacji w grafie.
# Złożoność: O(V + E).

from zad2testy import runtests

def breaking(G):
  n = len(G)

  visited = [False] * n
  parent = [-1] * n
  pre = [-1] * n
  low = [-1] * n
  preorder = 0

  max_vertex = None
  max_vertex_count = 0

  def dfs_visit(u):
    nonlocal preorder
    nonlocal max_vertex
    nonlocal max_vertex_count

    visited[u] = True

    pre[u] = low[u] = preorder
    preorder += 1

    count = 0
    for v, w in enumerate(G[u]):
      if w == 0:
        continue

      if not visited[v]:
        parent[v] = u
        dfs_visit(v)

        # Aktualizujemy najwyższy skok z podrzewa u.
        low[u] = min(low[u], low[v])

        # Jeżeli podrzewo zak. w v nie ma krawędzi wyżej niż u (tzn. low[v] < pre[u])
        # to dodajemy do count 1 bo całe podrzewo zostanie odłączone do grafu.
        if low[v] >= pre[u]:
          count += 1

      # Jeżeli wierzchołek jest odwiedzony i nie jest rodzicem u tzn. jest to krawędź wsteczna
      # do wierzchołka wyżej to aktualizujemy low[u].
      elif parent[u] != v:
        low[u] = min(low[u], pre[v])

    if count > max_vertex_count:
      max_vertex_count = count
      max_vertex = u

  dfs_visit(0)

  if max_vertex != 0:
    return max_vertex

  # Jeżeli max_vertex to korzeń drzewa to sprawdzamy czy ma więcej niż 1 podrzew.
  if max_vertex_count >= 2:
    return 0

  return None

runtests(breaking)

