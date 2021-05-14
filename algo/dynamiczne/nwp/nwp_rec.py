#!/usr/bin/env python3

def _nwp(s1, s2, c, b, i, j):
  if i < 0 or j < 0:
    return 0

  if c[i][j] < float("+inf"):
    return c[i][j]

  if s1[i] == s2[j]:
    v = _nwp(s1, s2, c, b, i - 1, j - 1) + 1
    c[i][j] = v
    b[i][j] = "cross"
    return v

  v1 = _nwp(s1, s2, c, b, i - 1, j)
  v2 = _nwp(s1, s2, c, b, i, j - 1)

  if v1 >= v2:
    c[i][j] = v1
    b[i][j] = "up"
    return v1
  else:
    c[i][j] = v2
    b[i][j] = "left"
    return v2

def nwp(s1, s2):
  n = len(s1)
  m = len(s2)

  c = [[float("+inf") for i in range(m)] for j in range(n)]
  b = [[float("+inf") for i in range(m)] for j in range(n)]

  v = _nwp(s1, s2, c, b, n - 1, m - 1)
  print(v)
  print_sol(b, s1, n - 1, m - 1)
  print()

def print_sol(b, s1, i, j):
  if i < 0 or j < 0:
    return

  if b[i][j] == "cross":
    print_sol(b, s1, i - 1, j - 1)
    print(s1[i], end="")
    return

  if b[i][j] == "up":
    return print_sol(b, s1, i - 1, j)

  if b[i][j] == "left":
    return print_sol(b, s1, i, j - 1)

