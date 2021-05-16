#!/usr/bin/env python3
#
# Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.
#

def dfs_visit(matrix, visited, i, j):
  visited[i][j] = True

  if i == len(matrix) - 1 and j == len(matrix) - 1:
    return True

  v = False
  for k, l in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    if i + k < 0 or i + k >= len(matrix) or j + l < 0 or j + l >= len(matrix):
      continue
    if matrix[i + k][j + l] > T and not visited[i + k][j + l]:
      v = v or dfs_visit(matrix, visited, i + k, j + l)
  return v

def solve(matrix):
  visited = [[False] * len(matrix) for _ in range(len(matrix))]
  return dfs_visit(matrix, visited, 0, 0)

matrix = [
  [0, 4, 1],
  [1, 4, 1],
  [0, 2, 4],
]

T = 3
print(solve(matrix))

