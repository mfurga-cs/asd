#!/usr/bin/env python3
#
# Heapsort
# Złożność: O(nlogn)

def left(i):
  return 2 * i + 1

def right(i):
  return 2 * i + 2

def parent(i):
  return (i - 1) // 2

def heapify(A, n, i):
  l = left(i)
  r = right(i)

  m = i
  if l < n and A[l] > A[m]:
    m = l
  if r < n and A[r] > A[m]:
    m = r

  if i != m:
    A[i], A[m] = A[m], A[i]
    heapify(A, n, m)

def build_heap(t, n):
  for i in range(parent(n - 1), -1, -1):
    heapify(A, n, i)

def heapsort(A):
  n = len(A)
  build_heap(A, n)

  for i in range(n - 1, 0, -1):
    A[0], A[i] = A[i], A[0]
    heapify(A, i, 0)

