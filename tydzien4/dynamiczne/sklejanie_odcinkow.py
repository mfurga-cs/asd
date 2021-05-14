#!/usr/bin/env python3

def f(dp, i, j):
  if dp[i][j]:
    return True

  v = False
  for k in range(i + 1, j):
    v = v or (f(dp, i, k) and f(dp, k, j))

  dp[i][j] = v
  return v

def res(p, i, j):
  c = max(p, key=lambda x: x[1])[1] + 1
  dp = [
    [False for i in range(c)]
    for j in range(c)
  ]

  for k in range(len(p)):
    dp[p[k][0]][p[k][1]] = True

  print(i, j)
  return f(dp, i, j)

p = [(1, 2), (4, 6), (5, 6), (2, 5), (6, 10)]
print(res(p, 4, 10))

