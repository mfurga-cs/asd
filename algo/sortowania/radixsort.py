#!/usr/bin/env python3
#
# Złożoność: O(d(n + k))
# n + k - złożoność countingsorta
# d - ilość powtórzeń countingsorta

def coutingsort(A, d):
  n = len(A)
  k = 10
  B = [0] * n
  C = [0] * k

  # Zliczamy ile razu dana liczba występuje.
  for i in range(n):
    C[(A[i] // d) % 10] += 1

  # C[i] - ile jest liczb <= i
  for i in range(1, k):
    C[i] += C[i - 1]

  for i in range(n - 1, -1, -1):
    C[(A[i] // d) % 10] -= 1
    B[C[(A[i] // d) % 10]] = A[i]

  for i in range(n):
    A[i] = B[i]

def radixsort(A):
  n = len(A)
  k = max(A)
  d = 1

  while k // d > 0:
    coutingsort(A, d)
    d *= 10

