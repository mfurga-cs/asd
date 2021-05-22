#!/usr/bin/env python3
#
# f(i) - najdłuższy rosnący ciąg kończący się na i-tym wyrazie.
#
# f(i) = max(0 <= j < i){ f(j) } + 1 jeśli A[j] < A[i]
# f(0) = 1

def result(A, P, i):
  if i == -1:
    return []
  return result(A, P, P[i]) + [A[i]]

def f(F, P, A, i):
  if i == 0:
    F[i] = 1
    return F[i]

  if F[i] is not None:
    return F[i]

  F[i] = 1
  for j in range(i):
    if A[j] < A[i]:
      v = f(F, P, A, j)
      if v + 1 > F[i]:
        F[i] = v + 1
        P[i] = j
  return F[i]

def fwrapper(A):
  n = len(A)
  F = [None] * n
  P = [-1] * n

  f(F, P, A, len(A) - 1)
  i = F.index(max(F))
  return result(A, P, i)

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
print(fwrapper(A))
print(lis(A))

