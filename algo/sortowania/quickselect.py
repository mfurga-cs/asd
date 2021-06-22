#!/usr/bin/env python3
#
# Szukanie i-tego co do wielkości elementu w czasie O(n) w nieposortowanie tablicy.
#
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

def _quickselect(A, l, r, k):
  if l == r:
    return A[l]
  q = partition(A, l, r)
  if q == k:
    return A[q]
  if q < k:
    return _quickselect(A, q + 1, r, k)
  if q > k:
    return _quickselect(A, l, q - 1, k)

def quickselect(A, k):
  return _quickselect(A, 0, len(A) - 1, k)

