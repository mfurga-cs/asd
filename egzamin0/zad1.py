#!/usr/bin/env python3
#
# Złożoność: O(n)
#

from collections import deque
from zad1testy import runtests

def tanagram(x, y, t):
  n = len(x)
  Q = [deque() for _ in range(0x100)]

  for i in range(t + 1):
    Q[ord(y[i])].append(i)

  for i in range(n):
    q = Q[ord(x[i])]

    if len(q) == 0:
      return False

    q.popleft()

    if i + t + 1 < n:
      Q[ord(y[i + t + 1])].append(i + t + 1)

    if i - t >= 0 and len(Q[ord(y[i - t])]) > 0 and Q[ord(y[i - t])][0] <= i - t:
      Q[ord(y[i - t])].popleft()

  return True

runtests(tanagram)

