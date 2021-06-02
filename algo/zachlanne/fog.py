#!/usr/bin/env python3

from queue import PriorityQueue
from zad1testy import runtests

def zbigniew(A):
  n = len(A)
  scope = 0
  count = 0

  V = [False] * n

  q = PriorityQueue()
  q.put((A[0], A[0]))

  while True:
    _, v = q.get()

    scope += v
    count += 1

    for i in range(scope + 1):
      if i == len(A):
        return count

      if V[i]:
        continue
      V[i] = True

      q.put((A[i] * -1, A[i]))

A = [2,2,1,0,0,0]
A = [4,5,2,4,1,2,1,0]

print(zbigniew(A))
#runtests(zbigniew)

