#!/usr/bin/env python3
#
# Alg. wyznacz przedziały które zawierają co najmniej jeden przedział.
# O(nlogn)
#

from collections import deque

def intersection(I):
  n = len(I)
  q = deque()
  s = []

  for i in range(n):
    I[i] = (I[i][0], I[i][1], i)

  I = sorted(I, key=lambda x: (x[0], -1 * x[1]))
  to_remove = []

  for i in range(n):
    if len(s) == 0 or s[-1][1] < I[i][1]:
      s.append(I[i])
      continue

    while len(s) > 0 and s[-1][1] >= I[i][1]:
      to_remove.append(s.pop()[2])

    #while len(s) > 0 and s[-1][1] < I[i][0]:
    #  s.pop()

    s.append(I[i])

  to_remove = sorted(to_remove)
  return to_remove

def intersection_brute(I):
  n = len(I)

  to_remove = []

  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      if I[i][0] <= I[j][0] and I[i][1] >= I[j][1]:
        to_remove.append(i)

  to_remove = sorted(list(set(to_remove)))
  return to_remove


import random

TESTS = 100_000

for i in range(TESTS):
  I = [tuple(sorted(random.sample(range(1, 10000), 2))) for _ in range(30)]
  I = list(set(I))

  I1 = I[:]
  I2 = I[:]

  r1 = intersection(I1)
  r2 = intersection_brute(I2)

  if r1 != r2:
    print(I)
    print(r1)
    print(r2)
    break

  print("[%d] OK" % (i), end="\r")

print()

