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

def _quickselect(arr, l, r, k):
  if l == r:
    return arr[l]

  p = partition(arr, l, r)

  if p == k:
    return arr[p]

  if p < k:
    return _quickselect(arr, l + 1, r, k)

  if p > k:
    return _quickselect(arr, l, r - 1, k)

def quickselect(arr, k):
  n = len(arr)
  return _quickselect(arr, 0, n - 1, k)

