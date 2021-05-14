#!/usr/bin/env python3
#
# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n),
# który stwierdza, czy w tablicy ponad połowa elementów ma jednakową wartość.

def half(t):
  n = len(t)
  l = t[0]
  i = 1

  for j in range(1, n):
    if i == 0:
      l = t[j]

    if t[j] == l:
      i += 1
    else:
      i -= 1

  return i > 1, l

