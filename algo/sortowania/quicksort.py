#!/usr/bin/env python3
#
# Quicksort.
#
# Złożoność: O(nlogn)
# Niestabilny

from random import randint

def partition(A, l, r):
  q = randint(l, r)
  A[q], A[r] = A[r], A[q]
  p = A[r]
  i = l - 1
  for j in range(l, r):
    if A[j] <= p:
      i += 1
      A[i], A[j] = A[j], A[i]
  A[i + 1], A[r] = A[r], A[i + 1]
  return i + 1

def _quicksort(A, l, r):
  if l < r:
    q = partition(A, l, r)
    _quicksort(A, l, q - 1)
    _quicksort(A, q + 1, r)

def quicksort(A):
  return _quicksort(A, 0, len(A) - 1)

