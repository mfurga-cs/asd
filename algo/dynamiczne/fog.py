#!/usr/bin/env python3
#
# f(i, y) - min. liczba skoków potrzebna by dotrzeć do liczby i mająć w zapasie dokładnie y
#           jednostek energii.
#
# f(i, y) = min(0 <= j < i) { f(j, max{ y + (i - j) - A[i], 0} } + 1
# f(0, y) = 0    gdy y <= 0
# f(0, y) = inf  gdy y >  0

from zad1testy import runtests

def result(P, A, i, y):
  if i == 0:
    return [0]
  j = P[i][y]
  return result(P, A, j, max(y + (i - j) - A[j], 0)) + [i]

def f(F, P, A, i, y):
  if i == 0:
    if y <= 0:
      return 0
    return float("+inf")

  if F[i][y] is not None:
    return F[i][y]

  F[i][y] = float("+inf")
  for j in range(i):
    v = f(F, P, A, j, max(y + (i - j) - A[j], 0))
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
    F[i] = [None] * (maxy + 1)
    P[i] = [None] * (maxy + 1)

  v = f(F, P, A, len(A) - 1, 0)
  return result(P, A, len(A) - 1, 0)

A = [2,2,1,0,0,0]
A = [4,2,2,4,1,2,1,0]
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A = [2,2,1,0,0,0]
A = [4,5,2,4,1,2,1,0]
print(fwrapper(A))

#runtests(fwrapper)


