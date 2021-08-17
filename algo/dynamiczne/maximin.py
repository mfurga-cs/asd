#!/usr/bin/env python3
#
# Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a1), (a1+1, . . . , a`2), ..., (a`k−1+1, . . . , an−1).
# Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy
# podciąg o najmniejszej wartości (rozstrzygając remisy w dowolny sposób). Wartością podziału
# jest wartość jego najgorszego podciągu. Zadanie polega na znalezienie podziału ciągu (a0, ..., an−1)
# o maksymalnej wartości.
# ---
#
# f(i, k) - maksymalna wartość podziału elementów 0 do i na k ciągów.
#           Wartość przedziału to ciąg w przedziale, który ma najmniejszą sumę elementów.
#
# f(i, k) = max(0 <= j < i){ min{ f(j, k - 1), sum(A[j+1:i]) } }
#

def result(P, A, i, k):
  if k == 1:
    return "|" + ",".join(str(n) for n in A[0:i+1])
  j = P[i][k]
  return result(P, A, j, k - 1) + "|" + ",".join(str(n) for n in A[j+1:i+1])

def s(A, i, j):
  return sum(A[i:j+1])

def f(F, P, A, i, k):
  if i == -1:
    return float("-inf")

  if k == 1:
    F[i][k] = s(A, 0, i)
    P[i][k] = 0
    return F[i][k]

  if F[i][k] is not None:
    return F[i][k]

  F[i][k] = float("-inf")
  for j in range(-1, i):
    v = min(f(F, P, A, j, k - 1), s(A, j + 1, i))
    if v > F[i][k]:
      F[i][k] = v
      P[i][k] = j
  return F[i][k]

def fwrapper(A, k):
  n = len(A)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    F[i] = [None] * (k + 1)
    P[i] = [None] * (k + 1)

  v = f(F, P, A, n - 1, k)
  print(v)
  return result(P, A, n - 1, k)

A = [2, 1, 3, 7, 5, 2, 3]
A = [2,2,2]
k = 3
print(fwrapper(A, k))

