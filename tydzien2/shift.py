#!/usr/bin/env python3

def shift(a, k):
  n = len(a)
  t = a[0]
  i = 0

  while True:
    p = (i + k) % n
    a[p], t = t, a[p]
    i = p
    if i == 0:
      break

