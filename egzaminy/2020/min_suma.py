#!/usr/bin/env python3

from zad2testy import runtests

def _opt_sum(arr, mem, sums, i, j):
  if i == j:
    return 0

  if i + 1 == j:
    return arr[i] + arr[i + 1]

  if mem[i][j] is not None:
    return mem[i][j]

  s = float("+inf")
  for k in range(i, j):
    v = _opt_sum(arr, mem, sums, i, k) + _opt_sum(arr, mem, sums, k + 1, j) + sums[j] - sums[i - 1]
    if v < s:
      s = v

  mem[i][j] = s
  return s

def opt_sum(arr):
  n = len(arr)
  mem = [[None for j in range(n)] for i in range(n)]

  sums = [arr[0]]
  for i in range(1, n):
    sums.append(arr[i] + sums[i - 1])

  print(sums)
  v = _opt_sum(arr, mem, sums, 0, n - 1)

  print()
  for row in mem:
    print(row)
  print()

  return v

t = [4, 1, 2, 3]
opt_sum(t)
#runtests(opt_sum)

