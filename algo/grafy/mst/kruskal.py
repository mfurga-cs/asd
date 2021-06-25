#!/usr/bin/env python3
# Alg. Kruskala - minimalne drzewo rozpinające dla grafów nieskierowanych!
# Zwraca listę krawędzi w postaci (u, v, w).
#
# Złożoność: O(ElogE) (sortowanie krawędzi)

from utils import g_convert

class Node(object):
  def __init__(self, value):
    self.value = value
    self.parent = self
    self.rank = 0

def find(x):
  if x != x.parent:
    x.parent = find(x.parent)
  return x.parent

def union(x, y):
  x = find(x)
  y = find(y)

  if x == y:
    return

  if x.rank > y.rank:
    y.parent = x
  else:
    x.parent = y
    if x.rank == y.rank:
      y.rank += 1

def edges(G):
  visited = [False] * len(G)
  E = []
  for u in range(len(G)):
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        E.append((u, v, w))
  return E

def kruskal(G):
  n = len(G)
  E = edges(G)

  # Sortujemy krawędzie po wagach.
  E = sorted(E, key=lambda x: x[2])
  V = [Node(i) for i in range(n)]

  result = []
  for u, v, w in E:
    # Dodajemy krawędź u, v do MST jeśli nie towrzy ona cylku z już wybranymi wierzchołkami.
    if find(V[u]) != find(V[v]):
      union(V[u], V[v])
      result.append((u, v, w))

  return result

G = """
0
1
2
3
4
#
0 1 10
1 2  1
2 3 3
2 0 4
0 4 100
3 4 20
"""

G = g_convert(G)
print(kruskal(G))

