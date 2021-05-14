#!/usr/bin/env python3

from random import randint, seed

def _merge(t, c, lo, mid, hi):
  for i in range(lo, hi + 1):
    c[i] = t[i]

  i, j = lo, mid + 1

  for k in range(lo, hi + 1):
    if i > mid:
      t[k] = c[j]; j += 1
    elif j > hi:
      t[k] = c[i]; i += 1
    elif c[i] <= c[j]:
      t[k] = c[i]; i += 1
    elif c[i] > c[j]:
      t[k] = c[j]; j += 1
  return t

def _mergesort(t, c, lo, hi):
  if lo >= hi:
    return
  mid = (lo + hi) // 2
  _mergesort(t, c, lo, mid)
  _mergesort(t, c, mid + 1, hi)
  return _merge(t, c, lo, mid, hi)

def mergesort(t):
  c = t[:]
  return _mergesort(t, c, 0, len(t) - 1)

seed(42)

n = 10
T = [randint(1,10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T) - 1):
  if T[i] > T[i + 1]:
    print("Błąd sortowania!")
    exit()

print("OK")

