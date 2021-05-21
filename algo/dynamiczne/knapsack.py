#!/usr/bin/env python3
#
# f(i, w) - max zysk jaki można uzyskać wybierając przedmioty od 0 do i mając w wolnego miejsca.
#

def result(dp, A, i, w):
  if i == 0:
    if w >= A[0][0]:
      return [A[0][1]]
    return []
  if w >= A[i][0] and dp[i][w] == dp[i - 1][w - A[i][0]] + A[i][1]:
    return get_solution(dp, A, i - 1, w - A[i][0]) + [A[i][1]]
  return get_solution(dp, A, i - 1, w)

def f(dp, A, i, w):
  if w < 0:
    return float("-inf")
  if i < 0:
    return 0

  if dp[i][w] is not None:
    return dp[i][w]

  dp[i][w] = max(f(dp, A, i - 1, w - A[i][0]) + A[i][1], f(dp, A, i - 1, w))
  return dp[i][w]

def knapsack(A, w):
  n = len(A)
  dp = [[None] * (w + 1) for _ in range(n)]
  f(dp, A, len(A) - 1, w)
  return get_solution(dp, A, len(A) - 1, w)

# (weight, cost)
A = [(12, 4), (6, 11), (4, 11), (3, 6)]
print(knapsack(A, 10))


