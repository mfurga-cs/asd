#!/usr/bin/env python3
#
# f(i, j) - min liczba mnożeń skalarnych aby obliczyć macierz do i do j.
#
# f(i, j) = min(i <= k < j) { f(i, k) + f(k + 1, j) + i * k * j }
# f(i, i) = 0

def result(P, A, i, j):
  if i == j:
    return str(i)
  k = P[i][j]
  return "(" + result(P, A, i, k) + result(P, A, k + 1, j) + ")"

def f(F, P, A, i, j):
  if i == j:
    return 0

  if F[i][j] is not None:
    return F[i][j]

  F[i][j] = float("+inf")
  for k in range(i, j):
    v = f(F, P, A, i, k) + f(F, P, A, k + 1, j) + A[i][0] * A[k + 1][0] * A[j][1]
    if v < F[i][j]:
      F[i][j] = v
      P[i][j] = k
  return F[i][j]

def fwrapper(A):
  n = len(A)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    F[i] = [None] * n
    P[i] = [None] * n

  v = f(F, P, A, 0, n - 1)
  print(result(P, A, 0, n - 1))
  return v

A = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
print(fwrapper(A))

