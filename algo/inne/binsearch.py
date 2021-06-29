#!/usr/bin/env python3
# Zwraca krotkę w postaci (bool, int). Jeśli bool = False to szukanego elementu nie ma
# w tablicy a int wskazuje index gdzie dany element powinnień się znaleźć. Jeśli
# bool = True to szukany element jest w tablicy a int wskazuje pierwsze wystąpienie
# danego elementu.

def binsearch(A, x):
  exists = False
  l = 0
  r = len(A) - 1
  while l <= r:
    m = (l + r) // 2
    if A[m] > x:
      r = m - 1
    if A[m] < x:
      l = m + 1
    if A[m] == x:
      exists = True
      r = m - 1
  return exists, l

if __name__ == "__main__":
  A = [1, 1, 2, 2, 2, 2, 2, 4]

  assert binsearch(A, 1) == (True, 0)
  assert binsearch(A, 2) == (True, 2)
  assert binsearch(A, 4) == (True, 7)
  assert binsearch(A, 0) == (False, 0)
  assert binsearch(A, -1) == (False, 0)
  assert binsearch(A, 3) == (False, 7)
  assert binsearch(A, 5) == (False, 8)
  assert binsearch(A, 6) == (False, 8)
  assert binsearch(A, 10) == (False, 8)

  A = []
  assert binsearch(A, 0) == (False, 0)
  assert binsearch(A, 1) == (False, 0)

  A = [1]
  assert binsearch(A, 1) == (True, 0)
  assert binsearch(A, 0) == (False, 0)
  assert binsearch(A, 2) == (False, 1)

  A = [float("+inf")]
  assert binsearch(A, 0) == (False, 0)
  assert binsearch(A, 100) == (False, 0)
  assert binsearch(A, -100) == (False, 0)

  A = [float("-inf")]
  assert binsearch(A, 0) == (False, 1)
  assert binsearch(A, 100) == (False, 1)
  assert binsearch(A, -100) == (False, 1)

  A = [float("+inf")] * 100
  assert binsearch(A, 0) == (False, 0)

  A = list(range(-1000, 1000))
  for num in range(-1000, 1000):
    assert binsearch(A, num) == (True, num + 1000)

  A = [e // 4 for e in range(1000)]
  for i in range(1000):
    assert binsearch(A, i // 4) == (True, A.index(i // 4))

