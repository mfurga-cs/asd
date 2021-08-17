#
# Sprawdzamy binary searchem.
#

def s(A, i, j):
  return sum(A[i:j+1])

def f(F, P, A, i, k):
  if i == -1:
    return float("-inf")

  if k == 1:
    F[i][k] = s(A, 0, i)
    P[i][k] = 0
    return F[i][k]

  if F[i][k] is not None:
    return F[i][k]

  F[i][k] = float("-inf")
  for j in range(-1, i):
    v = min(f(F, P, A, j, k - 1), s(A, j + 1, i))
    if v > F[i][k]:
      F[i][k] = v
      P[i][k] = j
  return F[i][k]

def sol2(A, k):
  n = len(A)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    F[i] = [None] * (k + 1)
    P[i] = [None] * (k + 1)

  return f(F, P, A, n - 1, k)

def is_ok(A, k, m):
  n = len(A)
  s = 0
  c = 0
  for i in range(n):
    if c == k:
      return True
    s += A[i]
    if s >= m:
      s = 0
      c += 1
  return c == k

def sol1(A, k):
  l = 0
  r = sum(A) // k
  res = 0

  while l <= r:
    m = (l + r) // 2
    if is_ok(A, k, m):
      res = m
      l = m + 1
    else:
      r = m - 1

  return res

from random import randint

A = [randint(1000000000, 1000000000000000000000000000000000000) for _ in range(500)]
k = 73
v1 = sol1(A, k)
print(v1)
v2 = sol2(A, k)
print(v2)
assert v1 == v2


