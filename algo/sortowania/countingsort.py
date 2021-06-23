#!/usr/bin/env python3
#
# Złożoność: O(n + k)
# Stabilny

def coutingsort(A):
  n = len(A)
  k = max(A) + 1
  B = [0] * n
  C = [0] * k

  # Zliczamy ile razu dana liczba występuje.
  for i in range(n):
    C[A[i]] += 1

  # C[i] - ile jest liczb <= i
  for i in range(1, k):
    C[i] += C[i - 1]

  for i in range(n - 1, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]

  for i in range(n):
    A[i] = B[i]

