#!/usr/bin/env python3
#
# f(i, j) - LCS ciągów od A[0..i] i B[0..j].
#
# f(i, j) = f(i - 1, j - 1) + 1             , jeśli A[i] == B[j]
# f(i, j) = max{ f(i - 1, j), f(i, j - 1) } , jeśli A[i] != B[j]
# f(i, j) = 0                               , jeśli i == 0 or j == 0

def result(P, A, B, i, j):
  if i < 0 or j < 0:
    return ""
  ii, jj = P[i][j]
  if i - 1 == ii and j - 1 == jj:
    return result(P, A, B, ii, jj) + A[i]
  return result(P, A, B, ii, jj)

def f(F, P, A, B, i, j):
  if i < 0 or j < 0:
    return 0

  if F[i][j] is not None:
    return F[i][j]

  if A[i] == B[j]:
    F[i][j] = f(F, P, A, B, i - 1, j - 1) + 1
    P[i][j] = (i - 1, j - 1)
    return F[i][j]

  v1 = f(F, P, A, B, i - 1, j)
  v2 = f(F, P, A, B, i, j - 1)

  if v1 >= v2:
    F[i][j] = v1
    P[i][j] = (i - 1, j)
  else:
    F[i][j] = v2
    P[i][j] = (i, j - 1)

  return F[i][j]

def fwrapper(A, B):
  n = len(A)
  m = len(B)

  F = [None] * n
  P = [None] * n
  for i in range(n):
    F[i] = [None] * m
    P[i] = [None] * m

  f(F, P, A, B, n - 1, m - 1)
  return result(P, A, B, n - 1, m - 1)

A = "alamakotaikotmapsa"
B = "kotmaalaikotaniema"
print(fwrapper(A, B))

