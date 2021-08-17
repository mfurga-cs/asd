#!/usr/bin/env python3

def permutations(A, perm=[]):
  if len(perm) == len(A):
    print(perm)
    return
  for i in range(len(A)):
    if i in perm:
      continue
    permutations(A, perm + [i])

permutations([1,2,3])


