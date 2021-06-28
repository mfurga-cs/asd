#!/usr/bin/env python3
# Mateusz Furga
# Wyznaczamy przedział quckselect dla przekatnej. h1 - elementy mniejsze od przekatnej, h
# h2 - elementy wieszke od przekatnej. Kopiujejmy elmenty spowrotem do T.
# Zloznosc O(n ** 2)


from zad1testy import runtests

def partition(arr, l, r):
  p = arr[r]
  i = l - 1

  for j in range(l, r):
    if arr[j] < p:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]

  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1

def _quickselect(arr, l, r, k):
  if l == r:
    return arr[l]

  p = partition(arr, l, r)

  if p == k:
    return arr[p]

  if p < k:
    return _quickselect(arr, l + 1, r, k)

  if p > k:
    return _quickselect(arr, l, r - 1, k)

def quickselect(arr, k):
  return _quickselect(arr, 0, len(arr) - 1, k)

def Median(T):
  t = T
  n = len(t)
  tmp = []

  mid = (n ** 2) // 2

  for i in range(n ** 2):
    tmp.append(t[i // n][i % n])

  if n % 2 == 1:
    p = mid - (n - 1) // 2
    q = mid + (n - 1) // 2
  else:
    p = mid - (n - 1) // 2 - 1
    q = mid + (n - 1) // 2

  pv = quickselect(tmp, p)
  qv = quickselect(tmp, q)

  m = (n ** 2 - n) // 2

  d = []
  h1 = []
  h2 = []

  for i in range(p, q + 1):
    d.append(quickselect(tmp, i))

  rest = []
  i = 0
  for i in range(n ** 2):
    if tmp[i] <= pv and len(h1) < m:
      h1.append(tmp[i])
    elif tmp[i] >= qv and len(h2) < m:
      h2.append(tmp[i])
    else:
      rest.append(tmp[i])

  while len(h1) < m:
    h1.append(rest.pop())

  while len(h2) < m:
    h2.append(rest.pop())

  k = 0
  for i in range(n ** 2):
    if i == k:
      T[i // n][i % n] = d.pop()
      k += (n + 1)
    elif (i % n) < (k % n):
      T[i // n][i % n] = h1.pop()
    else:
      T[i // n][i % n] = h2.pop()

runtests(Median)
