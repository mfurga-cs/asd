#!/usr/bin/env python3
# Binary search. Zwraca indeks pierwszego wystąpienia szukanego elementu lub -1 jeśli go nie ma.

def binary_search(A, x):
  result = -1
  l = 0
  r = len(A) - 1

  while l <= r:
    m = (l + r) // 2

    if A[m] > x:
      r = m - 1

    if A[m] < x:
      l = m + 1

    if A[m] == x:
      result = m
      r = m - 1

  return result

A = [1, 1, 2, 2, 2, 2, 2, 3]
print(binary_search(A, 3))

