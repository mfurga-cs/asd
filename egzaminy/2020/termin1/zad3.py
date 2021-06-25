#!/usr/bin/env python3
#
# Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x, gdzie a
# to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
# Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
# zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie
# jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
# obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
#

from math import log
from zad3testy import runtests

def insertionsort(A):
  n = len(A)
  for j in range(1, n):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] > key:
      A[i + 1] = A[i]
      i -= 1
    A[i + 1] = key

def bucketsort(A, a):
  n = len(A)
  m = n # ilość bucketów
  mini, maxi = min(A), max(A)

  B = [[] for _ in range(m)]

  for i in range(n):
    j = min(int(log(A[i], a) * m), m - 1)
    B[j].append(A[i])

  for i in range(m):
    insertionsort(B[i])

  k = 0
  for i in range(m):
    for j in range(len(B[i])):
      A[k] = B[i][j]
      k += 1

def fast_sort(A, a):
  bucketsort(A, a)
  return A

runtests(fast_sort)

