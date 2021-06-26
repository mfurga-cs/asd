#!/usr/bin/env python3

from math import log10

def count(n):
  t = n
  c = [0] * 10
  while n > 0:
    c[n % 10] += 1
    n //= 10
  j = 0
  w = 0
  for e in c:
    if e == 1:
      j += 1
    elif e > 1:
      w += 1
  return j, w, t

def countingsort(arr, n, m, k, reverse=False):
  c = [0] * m
  t = [0] * n

  for i in range(n):
    c[arr[i][k]] += 1

  for i in range(1, m):
    c[i] += c[i - 1]

  for i in range(n - 1, -1, -1):
    c[arr[i][k]] -= 1
    t[c[arr[i][k]]] = arr[i]

  if reverse:
    for i in range(n):
      arr[i] = t[n - i - 1]
  else:
    for i in range(n):
      arr[i] = t[i]

  return arr

def pretty_sort(arr):
  n = len(arr)
  t = []
  jmax, wmax = 0, 0

  for e in arr:
    j, w, e = count(e)
    jmax = max(jmax, j)
    wmax = max(wmax, w)
    t.append((j, w, e))

  jmax += 1
  wmax += 1

  print(t)
  countingsort(t, n, wmax, 1, True)
  countingsort(t, n, jmax, 0, True)
  print(t)

  for i in range(n):
    arr[i] = t[i][2]

  print(arr)

