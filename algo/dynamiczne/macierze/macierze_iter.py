#!/usr/bin/env python3

def print_parens(p, i, j):
  if i == j:
    print(x[i], end="")
  else:
    print("(", end="")
    print_parens(p, i, p[i][j])
    print_parens(p, p[i][j] + 1, j)
    print(")", end="")

def print_matrix(arr):
  for row in arr:
    print(row)

x = "ABCDEF"

def matrix_order(arr):
  n = len(arr)
  m = [[float("+inf") for i in range(n)] for j in range(n)]
  p = [[float("+inf") for i in range(n)] for j in range(n)]

  # Mnożenie macierzy przez samą siebie.
  for i in range(n):
    m[i][i] = 0

  for l in range(n):
    for i in range(n - l):
      # A = [A, B, C]
      # Generujemy przedziały A-A, B-B, C-C, A-B, B-C, A-C.
      j = i + l
      print(x[i], x[j])

      # Dzielimy przedział [i, j].
      # np. i = 0, j = 3:           [A, B, C, D]
      # ------------------------------------------------------------------
      # k = 0: [0, 0] i [1, 3]      [A] i [B, C, D]  -->  (A) * (B * C * D)
      # k = 1: [0, 1] i [2, 3]      [A, B] i [C, D]  -->  (A * B) * (C * D)
      # k = 2: [0, 2] i [3, 3]      [A, B, C] i [D]  -->  (A * B * C) * (D)
      for k in range(i, j):
        # Dodajemy koszt mnożenia np. (A * B * C) * (D * E)
        # X = (A * B * C) - min. koszt wyliczony wcześniej
        # Y = (D * E)     - min. koszt wyliczony wcześniej
        # I dodajemy koszt mnozenia X * Y.
        s = m[i][k] + m[k + 1][j] + arr[i][0] * arr[k + 1][0] * arr[j][1]
        if s < m[i][j]:
          m[i][j] = s
          p[i][j] = k

  print_matrix(m)
  return m[0][n - 1], p

t = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
res, p = matrix_order(t)

print_parens(p, 0, len(t) - 1)
print()


