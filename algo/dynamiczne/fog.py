#!/usr/bin/env python3
#
# f(i, y) - min. liczba skoków potrzebna by dotrzeć do liczby i mająć w zapasie dokładnie y
#           jednostek energii.
#
# f(i, y) = min(0 <= j < i) { f(j, y + (i - j) - A[i] } + 1
# f(0, y) = 0    gdy y <= A[0]
# f(0, y) = inf  gdy y >  A[0]

def result(P, A, i, y):
  if P[i][y] is None:
    return []
  return result(P, A, P[i][y], y + (i - P[i][y]) - A[i]) + [i]

def f(F, P, A, i, y):
  if i == 0 and y <= A[0]:
    return 0
  if i == 0:
    return float("+inf")

  if F[i][y] != float("+inf"):
    return F[i][y]

  F[i][y] = float("+inf")
  for j in range(i):
    v = f(F, P, A, j, y + (i - j) - A[i])
    if v + 1 < F[i][y]:
      F[i][y] = v + 1
      P[i][y] = j

  return F[i][y]

def fwrapper(A):
  n = len(A)
  F = [None] * n
  P = [None] * n

  maxy = sum(A)
  for i in range(n):
    F[i] = [float("+inf")] * (maxy + 1)
    P[i] = [None] * (maxy + 1)

  for y in range(A[0] + 1):
    F[0][y] = 0

  v = f(F, P, A, len(A) - 1, 0)
  return result(P, A, len(A) - 1, 0)

A = [2,2,1,0,0,0]
A = [4,2,2,4,1,2,1,0]
print(fwrapper(A))

