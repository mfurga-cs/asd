#!/usr/bin/env python3

def insertionsort(A):
  n = len(A)
  for j in range(1, n):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i + 1] = A[i]
      i -= 1
    A[i + 1] = key

def bucketsort(A):
  n = len(A)
  m = n # ilość bucketów
  mini, maxi = min(A), max(A)

  B = [[] for _ in range(m)]

  for i in range(n):
    j = min(int(((A[i] - mini) / (maxi - mini)) * m), m - 1)
    B[j].append(A[i])

  for i in range(m):
    insertionsort(B[i])

  k = 0
  for i in range(m):
    for j in range(len(B[i])):
      A[k] = B[i][j]
      k += 1

