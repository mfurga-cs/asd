#!/usr/bin/env python3
#
# Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
# zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
# funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
# z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
# zawsze prawidłowa.)
#

from zad3testy import runtests
from utils import BST

def binary_search(A, x):
  result = False
  l = 0
  r = len(A) - 1

  while l <= r:
    m = (l + r) // 2

    if A[m] > x:
      r = m - 1

    if A[m] < x:
      l = m + 1

    if A[m] == x:
      result = True
      r = m - 1

  return result, l

def longest_incomplete(A, k):
  n = len(A)
  bst = BST()

  # O(nlogk)
  for i in range(n):
    if bst.find(A[i]) == None:
      bst.insert(A[i])

  uniq = []
  count = [0] * k
  counter = 0

  # O(k)
  m = bst.min()
  while m is not None:
    uniq.append(m.value)
    bst.delete(m.value)
    m = bst.min()

  longest = 0
  i, j = 0, 0

  # O(nlogk)
  while j < n:
    _, idx = binary_search(uniq, A[j])
    if count[idx] == 0:
      counter += 1
    count[idx] += 1
    j += 1

    while counter == k:
      _, idx = binary_search(uniq, A[i])
      if count[idx] == 1:
        counter -= 1
      count[idx] -= 1
      i += 1

    longest = max(longest, j - i)

  return longest

runtests(longest_incomplete)

