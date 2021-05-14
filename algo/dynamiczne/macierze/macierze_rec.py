#!/usr/bin/env python3

def mem_matrix_order(arr):
  n = len(arr)
  m = [[float("+inf") for i in range(n)] for j in range(n)]
  return _mem_matrix_order(arr, m, 0, n - 1)

def _mem_matrix_order(arr, m, i, j):
  if i == j:
    m[i][j] = 0
    return 0

  if m[i][j] < float("+inf"):
    return m[i][j]

  s = float("+inf")
  for k in range(i, j):
    q = _mem_matrix_order(arr, m, i, k) + _mem_matrix_order(arr, m, k + 1, j) + arr[i][0] * arr[k + 1][0] * arr[j][1]
    if q < s:
      s = q

  m[i][j] = s
  return s

t = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]


