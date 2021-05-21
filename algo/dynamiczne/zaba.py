#!/usr/bin/env python3
#
# f(i, y) - min. liczba skoków potrzebna by dotrzeć do liczby i mająć w zapasie dokładnie y
#           jednostek energii.

def f(A, i, y):
  if i == 0 and y <= A[0]:
    return 0
  if i == 0:
    return float("+inf")
  k = float("+inf")
  for j in range(i):
    k = min(k, f(A, j, y + (i - j) - A[i]))
  return k + 1

def fog(A):
  n = len(A)
  F = [None] * n
  P = [None] * n

  maxy = sum(A)
  for i in range(n):
    F[i] = [float("+inf")] * (maxy + 1)

  for y in range(A[0] + 1):
    F[0][y] = 0

  for i in range(n):
    for y in range(maxy):
      for j in range(i):
        if maxy >= y + (i - j) - A[i] >= 0 and F[j][y + (i - j) - A[i]] + 1 < F[i][y]:
          F[i][y] = F[j][y + (i - j) - A[i]] + 1
          P[i] = j

  for row in F:
    print(row)

  print(P)

  i = len(A) - 1
  l = []
  while i != None:
    l.insert(0, i)
    i = P[i]

  print(l)

A = [2,2,1,0,0,0]
A = [4,5,2,4,1,2,1,0]
fog(A)


