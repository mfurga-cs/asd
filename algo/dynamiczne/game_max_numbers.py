#!/usr/bin/env python3
#
# Dostajemy tablicę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną libczę
# z końców tablicy potem robi to przeciwnik. Naszym zadaniem jest wyliczenie max sumy
# liczb jakie możemy w ten sposób uzyskać zakładając że przeciwnik gra optymalnie.
#

def f(F, A, i, j):
  if i + 1 == j:
    return max(A[i], A[j])
  if i == j:
    return A[i]
  #if i > j:
  #  return 0

  if F[i][j] is not None:
    return F[i][j]

  F[i][j] = max(A[i] + min(f(F, A, i + 2, j), f(F, A, i + 1, j - 1)), \
                A[j] + min(f(F, A, i, j - 2), f(F, A, i + 1, j - 1)))
  return F[i][j]

from random import randint
A = [randint(0, 100) for _ in range(300)]

n = len(A)
F = [[None] * n for _ in range(n)]
v = f(F, A, 0, len(A) - 1)

print("sum\t", sum(A))
print("p1\t", v)
print("p2\t", sum(A) - v)
print("diff\t", 2 * v - sum(A))


