#!/usr/bin/env python3

def search(arr, p, e):
  i = 0
  j = len(p) - 1
  while i <= j:
    m = (i + j) // 2
    if p[m] > e:
      j = m - 1
    elif p[m] < e:
      i = m + 1
    else:
      return m
  return i

def lis(arr):
  n = len(arr)
  p = [float("+inf")] * (n + 1)
  p[0] = float("-inf")

  k = 0
  for i in range(n):
    j = search(arr, p, arr[i])
    k = max(k, j)
    p[j] = arr[i]

  print(p)
  return k


