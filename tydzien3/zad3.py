#/usr/bin/env python3

from random import randint, shuffle, seed

def _insertion_sort(arr, lo, hi):
  # Insertion sort dla elementów od lo do hi.
  for i in range(lo + 1, hi + 1):
    key = arr[i]
    j = i - 1
    while j >= lo and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key

def _partition(arr, lo, hi):
  # Lomuto partition scheme.
  p = arr[hi]
  i = lo - 1
  for j in range(lo, hi):
    if arr[j] < p:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
  return i + 1

def _median(arr, lo, hi):
  # Funkcja wybiera pivot przy użyciu algorytmu magicznych piątek.
  j = lo

  for i in range(lo, hi + 1, 5):
    # Sortujemy kolejne 5-tki.
    _insertion_sort(arr, i, min(i + 4, hi))
    median = (i + min(i + 4, hi)) // 2

    # Mediany wrzucamy na początek tablicy.
    arr[j], arr[median] = arr[median], arr[j]
    j += 1

  pivot = None

  if j - lo <= 5:
    # Jeżeli ilość median <= 5 to sortujemy i zwracamy pivot.
    _insertion_sort(arr, lo, j - 1)
    pivot = lo + (j - lo) // 2
  else:
    # Jeżeli nie to wykonujemy rekurencyjnie funkcje dla początku tablicy gdzie
    # znajdują się znalezione mediany.
    pivot = _median(arr, lo, j - 1)

  return pivot

def linearselect(arr, k):
  lo, hi = 0, len(arr) - 1

  while True:
    # Szukamy pivota (indeksu) i wrzucamy go na koniec tablicy.
    pivot = _median(arr, lo, hi)
    arr[hi], arr[pivot] = arr[pivot], arr[hi]

    # Wykonujemy partition dla znalezionego pivota.
    p = _partition(arr, lo, hi)

    if p == k:
      return arr[p]

    if p < k:
      lo = p + 1
    else:
      hi = p - 1

seed(42)

n = 11
for i in range(n):
  A = list(range(n))
  shuffle(A)
  print(A)
  x = linearselect( A, i )
  if x != i:
    print("Blad podczas wyszukiwania liczby", i)
    exit(0)

print("OK")

