#!/usr/bin/env python3
#
# f(i, s) - czy istnieje ciąg liczb 0..i sumujący się do s.
#
# f(i, 0) = 1      | jeśli s = 0
# f(i, s) = 0      | jeśli i < 0 lub s < 0
# f(i, s) = max(f(i - 1, s - a[i]), f(i - 1, s))
#
# f(n - 1, t) - rozwiązanie.
# O(n * t)

from random import randint

NOT_CALCULATED = None

mem = []

def _subset_sum(nums, i, s):
  if s == 0:
    return True

  if i < 0 or s < 0:
    return False

  if mem[i][s] is NOT_CALCULATED:
    mem[i][s] = _subset_sum(nums, i - 1, s - nums[i]) or _subset_sum(nums, i - 1, s)

  return mem[i][s]

def subset_sum(nums, s):
  global mem
  n = len(nums)
  mem = [[NOT_CALCULATED for _ in range(s + 1)] for _ in range(n)]
  return _subset_sum(nums, len(nums) - 1, s)

def subset_sum2(nums, t):
  n = len(nums)
  F = [[NOT_CALCULATED for _ in range(t + 1)] for _ in range(n + 1)]

  for i in range(t + 1):
    F[-1][i] = False

  for i in range(n + 1):
    F[i][0] = True

  for i in range(n):
    for s in range(1, t + 1):

      if nums[i] > s:
        res = F[i - 1][s]
      else:
        res = F[i - 1][s] or F[i - 1][s - nums[i]]

      #res = F[i - 1][s]
      #if s - nums[i] >= 0:
      #  res = res or F[i - 1][s - nums[i]]
      F[i][s] = res

  for row in F:
    print(row)
  return F[n - 1][t]

