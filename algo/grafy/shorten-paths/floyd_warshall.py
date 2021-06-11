#!/usr/bin/env python3

def get_shorest_path(P, i, j):
  if i == j:
    return [i]
  # Nie istnieje scieżka z i do j. Nie zmieniać kolejności! (nie wypisze pierwszego wierzchołka)
  if P[i][j] == -1:
    return []
  return get_shorest_path(P, i, P[i][j]) + [j]

def floyd_warshall(G):
  n = len(G)
  D = [row[:] for row in G]
  P = [row[:] for row in G]

  # D[u][v] = 0 or W[u][v] or +inf
  for u in range(n):
    for v in range(n):
      P[u][v] = -1

      if u != v and G[u][v] == 0:
        D[u][v] = float("+inf")

      if u != v and G[u][v] != 0:
        P[u][v] = u

  for k in range(n):
    for u in range(n):
      for v in range(n):
        if D[u][v] > D[u][k] + D[k][v]:
          D[u][v] = D[u][k] + D[k][v]
          P[u][v] = P[k][v]

  for row in D:
    print(row)

  print("-----")
  #print(D[2][3])
  #p = get_shorest_path(P, 2, 3)
  #print(p)

G = [
  [0, 4, 0, 0],
  [0, 0, 0, -2],
  [2, 0, 0, 0],
  [2, 0, 0, 0]
]

G = [
  [0, 5, 0],
  [0, 0, 2],
  [-8, 0, 0]
]

floyd_warshall(G)

