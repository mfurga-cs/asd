#!/usr/bin/env python3
#
# f(i, y) - min. liczba skoków potrzebna by dotrzeć do liczby i mająć w zapasie dokładnie y
#           jednostek energii.

from zad1testy import runtests

def f(A, i, y):
  if i == 0 and y <= 0:
    return 0

  if i == 0:
    return float("+inf")

  #if y < 0:
  #  return float("+inf")

  k = float("+inf")
  for j in range(i):
    k = min(k, f(A, j, y + (i - j) - A[j]))
  return k + 1

def f2(A, i, n, y=0):
  if i == n and y >= 0:
    return 0
  if i > n:
    return float("+inf")
  y += A[i]
  k = float("+inf")
  for j in range(1, y + 1):
    k = min(k, f2(A, i + j, n, y - j))
  return k + 1

def result(A):
  n = len(A)
  v = float("+inf")
  for i in range(13):
    v = min(v, f(A, n - 1, i))
  return v
  #return f2(A, 0, len(A) - 1)

A = [3, 0, 0, 0, 1]
print(f(A, len(A) - 1, 0))

runtests(result)


