#!/usr/bin/env python3

from math import *

def tspf(F, D, B, i, j):
  if F[i][j] != float("+inf"):
    return F[i][j]

  if i == j - 1:
    F[j - 1][j] = float("+inf")
    for k in range(j - 1):
      q = tspf(F, D, B, k, j - 1) + D[k][j]
      if q < F[j - 1][j]:
        F[j - 1][j] = q
        B[j - 1][j] = k
  else:
    F[i][j] = tspf(F, D, B, i, j - 1) + D[j - 1][j]
    B[i][j] = j - 1
  return F[i][j]

def build_path(C, B, i, j, p):
  if i < j:
    print("calling (%i, %i)" % (i, j))
    k = B[i][j]
    print("k=", k)
    if k >= 0:
      p.insert(0, C[k][0])
      print("insert (%s)\n" % (C[k][0]))
      build_path(C, B, i, k, p)
  else:
    print("calling (%i, %i)" % (j, i))
    k = B[j][i]
    print("k=", k)
    if k >= 0:
      print("append (%s)\n" % (C[k][0]))
      p.append(C[k][0])
      build_path(C, B, k, j, p)

def bitonicTSP(C):
  n = len(C)
  C = sorted(C, key=lambda x: x[1])
  D = []

  for i in range(n):
    d = []
    for j in range(n):
      d.append(((C[i][1] - C[j][1]) ** 2 + (C[i][2] - C[j][2]) ** 2) ** (1/2.) )
    D.append(d)

  F = [[float("+inf")] * n for i in range(n)]
  F[0][1] = D[0][1]

  B = [[-1] * n for i in range(n)]

  print(C)

  j = - 1
  m = float("+inf")
  for i in range(n - 1):
    v = tspf(F, D, B, i, n - 1) + D[i][n - 1]
    if v <= m:
     m = v
     j = i

  print(m)
  path = []
  path.append(C[n - 1][0])
  path.insert(0, C[j][0])

  #print(j, n - 1)

  print(path)
  build_path(C, B, n - 1, j, path)
  #path.append(C[0][0])

  print(path)


C = [
  ("Wrocław", 0, 2),
  ("Sopot", 5, 2),
  ("Gdańsk", 10, 6),
  ("Kraków", 2, 0),
  ("Poznań", 4, 4),
  ("Radom", 3, 1),
]

C = [["Wrocław", 0, 2], ["Warszawa",4,3],["Gdańsk", 2,4], ["Kraków",6,1], ["Paprykarz", 3, 1]]

bitonicTSP(C)

