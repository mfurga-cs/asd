#!/usr/bin/env python3

from random import randint

def sumsort(A, n):
  m = n ** 2
  B = [0] * m
  sums = [0] * n

  # O(n^2)
  for i in range(m):
    sums[i // n] += A[i]

  # O(n)
  for i in range(n):
    sums[i] = (sums[i], i)

  # O(nlogn)
  sums = sorted(sums, key=lambda x: x[0])
  print(sums)

  # O(n^2)
  k = 0
  for i in range(n):
    idx = sums[i][1]

    for j in range(n):
      B[k] = A[n * idx + j]
      k += 1

  print(B)

