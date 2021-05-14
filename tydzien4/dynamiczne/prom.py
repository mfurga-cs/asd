#!/usr/bin/env python3
#
# f(i, L, R) - czy da się załadować od 0 do i samochodów na prom mając L miejsca na lewym i R
#              miejsca na prawym pasie.
#
# Odp: max{i | f(i, L, L) == 1}
#
def dp(A, i, l, r):
  if l < 0 or r < 0:
    return False

  if i == 0:
    if l - A[i] >= 0 or r - A[i] >= 0:
      return True
    else:
      return False

  return dp(A, i - 1, l - A[i], r) or dp(A, i - 1, l, r - A[i])


A = [6, 3, 4, 2, 1, 1]
L = 6

v = float("-inf")
for i in range(len(A)):
  if dp(A, i, L, L):
    v = max(v, i)

print(v + 1)



