#!/usr/bin/env python3
#
# f(i, k) - min. liczba skoków potrzebna aby dotrzeć na pole i-te i mając na nim po
#           zjedzeniu k jednostek energii.
#
# f(i, k) = min(f(j, k + (i - j) - A[i]) + 1)
# Musimy zadbać o to aby energie na polu i-tym nie była mniejsza niż wartość na nim.
# Tzn. k = max(k + (i - j) - A[i], A[j])
#
# ODP: f(n - 1, A[n - 1])

from zad1testy import runtests

def get_solution(A, P, i, k):
  if P[i][k] is None:
    return [i]
  ii, kk = P[i][k]
  kk = max(kk, A[ii])
  return get_solution(A, P, ii, kk) + [i]

def f(F, P, A, i, k):
  if i == 0:
    if k <= A[0]:
      return 0
    return float("+inf")

  # Nie możemy mieć mniej energii na polu i-tym niż A[i].
  if k < A[i]:
    k = A[i]

  if F[i][k] is not None:
    return F[i][k]

  F[i][k] = float("+inf")
  for j in range(i):
    v = f(F, P, A, j, k + (i - j) - A[i]) + 1
    if v < F[i][k]:
      F[i][k] = v
      P[i][k] = (j, k + (i - j) - A[i])
  return F[i][k]

def fwrapper(A):
  n = len(A)
  s = sum(A)
  F = [None] * n
  P = [None] * n
  for i in range(n):
    F[i] = [None] * s
    P[i] = [None] * s
  v = f(F, P, A, n - 1, A[n - 1])
  print(get_solution(A, P, n - 1, A[n - 1]))
  return v

runtests(fwrapper)

