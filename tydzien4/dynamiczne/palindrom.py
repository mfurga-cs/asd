#!/usr/bin/env python3

def _palindrom(s, p, i, j):
  if i > j:
    return 0
  if i == j:
    return 1
  if s[i] == s[j]:
    p[i][j] = (i + 1, j - 1)
    return _palindrom(s, p, i + 1, j - 1) + 2
  v1 = _palindrom(s, p, i + 1, j)
  v2 = _palindrom(s, p, i, j - 1)
  if v1 >= v2:
    p[i][j] = (i + 1, j)
    return v1
  p[i][j] = (i, j - 1)
  return v2

p = None

def palindrom(s):
  global p
  n = len(s)
  p = [[(-1, -1) for j in range(n)] for i in range(n)]
  v =_palindrom(s, p, 0, n - 1)

  for row in p:
    print(row)

  print_solution(s, p, 0, n - 1)
  print(c)

  return v

