#!/usr/bin/env python3

from inttree import *

def intervals(I):
  A = []
  for interval in I:
    A.append(interval[0])
    A.append(interval[1])
  A = sorted(A)

  i = 0; j = 0
  while j < len(A):
    while j + 1 < len(A) and A[j] == A[j + 1]:
      j += 1
    A[i] = A[j]
    i += 1
    j += 1
  A = A[:i]

  T = tree(A)
  tree_insert(T, I[0])
  result = [I[0][1] - I[0][0]]

  for interval in I[1:]:
    a, b = interval
    left = tree_intersect(T, a)
    right = tree_intersect(T, b)

    best_left = None
    best_right = None

    for l in left:
      if l[0] < a:
        a = l[0]
        best_left = l

    for r in right:
      if r[1] > b:
        b = r[1]
        best_right = r

    if best_left is not None:
      tree_remove(T, best_left)

    if best_right is not None:
      tree_remove(T, best_right)

    tree_insert(T, (a, b))
    result.append(max(b - a, result[-1]))

  return result

run_tests(intervals)


