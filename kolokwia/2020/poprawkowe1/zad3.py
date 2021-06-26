#!/usr/bin/env python3
#
# Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
# zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
# funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
# z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
# zawsze prawidłowa.)
#

from zad3testy import runtests

def all_usage(U, uniq):
  count = 0
  for i in uniq:
    if U[i] > 0:
      count += 1
  return count == len(uniq)

def longest_incomplete(A, k):
  n = len(A)
  maxi = max(A) + 1

  uniq = list(set(A))

  #U = [0] * maxi
  U = {}

  for i in range(n):
    if A[i] not in U:
      U[A[i]] = 0

  #for i in range(n):
  #  C[A[i]] = 1

  longest = 0
  i, j = 0, 0

  while j < n:
    U[A[j]] += 1
    j += 1

    while all_usage(U, uniq):
      U[A[i]] -= 1
      i += 1

    longest = max(longest, j - i)

  return longest

runtests(longest_incomplete)

