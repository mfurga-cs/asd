#!/usr/bin/env python3
#
# f(i) - najdłuższy rosnący ciąg kończący się na i-tym wyrazie.
#

def f(A, i):
  if i == 0:
    return 1
  v = 0
  for j in range(i):
    if A[j] < A[i]:
      v = max(v, f(A, j))
  return v + 1

def result(A, P, i):
  if i == -1:
    return []
  return result(A, P, P[i]) + [A[i]]

def lis(A):
  n = len(A)
  F = [1] * n
  P = [-1] * n

  for i in range(n):
    for j in range(i):
      if A[j] < A[i] and F[j] + 1 > F[i]:
        F[i] = F[j] + 1
        P[i] = j

  i = F.index(max(F))
  return result(A, P, i)

A = [13, 7, 21, 42, 8, 2, 44, 53]
print(f(A, len(A) - 1))
print(lis(A))

