#!/usr/bin/env python3
#
# f(i, p) - min. waga przedmiotów od 0..i dla których zysk = p.
#
# f(i, 0) = 0
# f(0, p) = +inf    jeśli P[0] != p
# f(0, p) = W[0]    jeśli P[0] = p
#
# f(i, p) = min(f(i - 1, p), f(i - 1, p - P[i]) + W[i])
#
# ODP: max p dla którego F[n - 1][p] <= s

def get_solution(P, W, F, i, j):
  if j == 0:
    return []
  if i == 0:
    if F[i][j] < float("+inf"):
      return [i]
    return []
  v1 = F[i - 1][j]
  v2 = float("+inf")
  if j - P[i] >= 0:
    v2 = F[i - 1][j - P[i]] + W[i]
  if v1 <= v2:
    return get_solution(P, W, F, i - 1, j)
  return get_solution(P, W, F, i - 1, j - P[i]) + [i]

def knapsack(P, W, s):
  n = len(P)
  p = sum(P)
  F = [[float("+inf")] * (p + 1) for _ in range(n)]

  for i in range(n):
    F[i][0] = 0

  for i in range(n):
    for j in range(p + 1):
      res = F[i - 1][j]
      if j - P[i] >= 0:
        res = min(res, F[i - 1][j - P[i]] + W[i])
      F[i][j] = res

  max_p = -1

  for j in range(p, -1, -1):
    if F[n - 1][j] <= s:
      max_p = j
      break

  print("W: ", W)
  print("P: ", P)
  print("i: %i, max_prof: %i" % (i, j))
  s = get_sol(P, W, F, i, j)
  print(s)

P = [3, 1, 2, 4]
W = [2, 1, 4, 1]

