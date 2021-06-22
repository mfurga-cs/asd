#!/usr/bin/env python3
#
# Insertion sort.
#
# Złożoność: O(n ^ 2)
# Stabilny

def insertionsort(A):
  n = len(A)
  for j in range(1, n):
    key = A[j]
    i = j - 1
    # Wstawiamy A[j] w posortowany już ciąg A[0..j-1].
    while i >= 0 and A[i] > key:
      A[i + 1] = A[i]
      i -= 1
    A[i + 1] = key

