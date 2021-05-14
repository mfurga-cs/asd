#!/usr/bin/env python3

def countingsort(a, n, e, b=10):
  c = [0] * b
  t = [0] * n

  for i in range(n):
    c[(a[i] // e) % b] += 1

  for i in range(1, b):
    c[i] += c[i - 1]

  for i in range(n - 1, -1, -1):
    c[(a[i] // e) % b] -= 1
    t[c[(a[i] // e) % b]] = a[i]

  for i in range(n):
    a[i] = t[i]

  return a

def radixsort2(a):
  # O(d(n + b))
  n = len(a)
  b = n

  countingsort(a, n, 1, n)
  countingsort(a, n, n, n)

#def radixsort1(a):
#  n = len(a)
#  m = max(a)
#  e = 1
#  while m // e > 0:
#    countingsort(a, n, e)
#    e *= 10

