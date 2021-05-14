#!/usr/bin/env python3

# f(i, k) - maksymalna wartość podziału elementów 0 do i na k ciągów.
# wartość przedziału to ciąg w przedziale, który ma najmniejszą sumę elementów.
#
# f(i, k) = max(0 do i - 1){ min{ f(j, k - 1), suma od j + 1 do i } }
#

def s(A, i, j):
  return sum(A[i:j+1])

def dp(A, i, t):
  if i == -1:
    return float("-inf")

  if t == 1:
    return s(A, 0, i)

  v = float("-inf")
  for j in range(-1, i):
    v = max(v, min(dp(A, j, t - 1), s(A, j + 1, i)))
  return v

A = [2, 1, 3, 7, 5, 2, 3]
v = dp(A, len(A) - 1, 3)
print(v)


