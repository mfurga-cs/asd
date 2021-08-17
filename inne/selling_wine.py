#!/usr/bin/env python3
#
# A = [2, 4, 6, 2, 5]
#
# f(i, j) - max. zysk ze sprzedaży win od i do j
# f(i, j) = max{ f(i + 1, j) + A[i] * k, f(i, j - 1) + A[j] * k }
#
def profit(A, i, j):
  if i > j:
    return 0
  k = len(A) - (j - i)
  return max(profit(A, i + 1, j) + A[i] * k, profit(A, i, j - 1) + A[j] * k)


def wine(A):
  n = len(A)

  dp = [None] * n
  for i in range(n):
    dp[i] = [None] * n

  for i in range(n):
    dp[i][i] = A[i] * n

  for i in range(n - 1, -1, -1):
    for j in range(i, n - 1):
      k = n - (j - i)
      print(i, j, k)
      print(i - 1, j + 1, k)
      dp[i][j] = max(dp[i + 1][j] + A[i] * k, dp[i][j - 1] + A[j] * k)

  return dp[0][n - 1]

A = [2, 4, 6, 2, 5]
n = len(A)
print(profit(A, 0, n - 1))
print(wine(A))

