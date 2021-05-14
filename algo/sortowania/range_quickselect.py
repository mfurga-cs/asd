#!/usr/bin/env python3

from random import randint

def partition(arr, l, r):
  q = randint(l, r)
  arr[q], arr[r] = arr[r], arr[q]

  p = arr[r]
  i = l - 1

  for j in range(l, r):
    if arr[j] < p:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1

def _quickselect(arr, l, r, i, j):
  if r - l <= j - i:
    return l

  p = partition(arr, l, r)

  if p > j:
    return _quickselect(arr, i, j, l, p - 1)

  if p < i:
    return _quickselect(arr, i, j, p + 1, r)

  return p

def quickselect(arr, i, j):
  n = len(arr)
  t = arr[:]
  _quickselect(t, 0, n - 1, i, j)
  print(t)

