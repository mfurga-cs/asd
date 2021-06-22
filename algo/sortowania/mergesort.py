#!/usr/bin/env python3
# Mergesort.
#
# Złożoność: O(nlogn)
# Stabilny

def merge(A, C, l, m, r):
  for i in range(l, r + 1):
    C[i] = A[i]

  i, j = l, m + 1

  for k in range(l, r + 1):
    if i > m:
      A[k] = C[j]; j += 1
    elif j > r:
      A[k] = C[i]; i += 1
    elif C[i] <= C[j]:
      A[k] = C[i]; i += 1
    elif C[i] > C[j]:
      A[k] = C[j]; j += 1

def _mergesort(A, C, l, r):
  if l < r:
    m = (l + r) // 2
    _mergesort(A, C, l, m)
    _mergesort(A, C, m + 1, r)
    merge(A, C, l, m, r)

def mergesort(A):
  C = A[:]
  return _mergesort(A, C, 0, len(A) - 1)

