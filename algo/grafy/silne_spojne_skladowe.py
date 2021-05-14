#!/usr/bin/env python3

def transpose(G):
  n = len(G)
  T = [[] for _ in range(n)]
  for u in range(n):
    for v in G[u]:
      T[v].append(u)
  return T

def dfs_visit(G, u, visited, finished):
  visited[u] = True
  for v in G[u]:
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
  T = transpose(G)

  # Wykonujemy DFS dla grafu T w kolejności majejących czasów przetworzeń G.
  # Czyli od wierzchołków które były ostanie przetowrzone.
  visited = [False] * len(T)

  for u in finished[::-1]:
    if not visited[u]:
      # Wszystkie wierzchołki które będą odwiedzone przy tym wywołaniu będą najeżeć do
      # jeden spójnej składowej (comp).
      comp = []
      dfs_visit(T, u, visited, comp)
      print(comp)

G = [
  [1],
  [2],
  [0, 3],
  [4],
  [5],
  [6],
  [3]
]

scc(G)

