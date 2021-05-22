#!/usr/bin/env python3
#
# f(i, w) - max zysk jaki można uzyskać wybierając przedmioty od 0 do i mając w wolnego miejsca.
#
# f(i, w) = max{ f(i - 1, w - W[i]) + P[i], f(i - 1, w) }
# f(0, w) = P[0] jeśli w >= W[0]
# f(0, w) = -inf jeśli w <  W[0]

# Result bez parentów.
def result(F, A, i, w):
  if i == 0:
    if w >= A[0][0]:
      return [A[0][1]]
    return []
  if w >= A[i][0] and F[i][w] == F[i - 1][w - A[i][0]] + A[i][1]:
    return result(F, A, i - 1, w - A[i][0]) + [A[i][1]]
  return result(F, A, i - 1, w)

# Result z parentami.
def result(P, A, i, w):
  if P[i][w] is None:
    return []
  if P[i][w]:
    return result(P, A, i - 1, w - A[i][0]) + [A[i][1]]
  return result(P, A, i - 1, w)

def f(F, P, A, i, w):
  if w < 0:
    return float("-inf")
  if i < 0:
    return 0

  if F[i][w] is not None:
    return F[i][w]

  v1 = f(F, P, A, i - 1, w - A[i][0]) + A[i][1]
  v2 = f(F, P, A, i - 1, w)

  P[i][w] = v1 > v2
  F[i][w] = max(v1, v2)

  return F[i][w]

def knapsack(A, w):
  n = len(A)
  F = [None] * n
  P = [False] * n

  for i in range(n):
    F[i] = [None] * (w + 1)
    P[i] = [None] * (w + 1)

  f(F, P, A, len(A) - 1, w)
  return result(P, A, len(A) - 1, w)

# (weight, cost)
A = [(12, 4), (6, 11), (4, 11), (3, 6)]
print(knapsack(A, 7))


