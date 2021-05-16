#!/usr/bin/env python3

def subset(dp, A, i, s):
  if s < 0:
    return False

  if dp[i][s] is not None:
    return dp[i][s]

  dp[i][s] = subset(dp, A, i - 1, s - A[i]) or subset(dp, A, i - 1, s)
  return dp[i][s]

def main(A, s):
  dp = [[None] * (s + 1) for _ in range(len(A))]

  for i in range(s + 1):
    dp[0][i] = False

  if A[0] <= s:
    dp[0][A[0]] = True

  for i in range(len(A)):
    dp[i][0] = True

  subset(dp, A, len(A) - 1, s)

  for row in dp:
    print(row)

  return dp[len(A) - 1][s]

A = [4, 0, 3, 6, 6]

print(main(A, 7))


