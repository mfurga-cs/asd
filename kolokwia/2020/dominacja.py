#!/usr/bin/env python3

def dominance(arr):
  n = len(arr)

  s = []

  x = sorted(arr, key=lambda e: e[0])
  y = sorted(arr, key=lambda e: e[1])

  print(x)
  print(y)

  for i in range(n):
    if x[i] is not None:
      #s.append(x[i])
      s.append(arr.index(x[i]))

      remove = False
      # usuwamy z y
      for j in range(n):
        if y[j] == x[i]:
          remove = True
        if remove:
          y[j] = None

      # usuwamy z x
      for j in range(i, n):
        if x[j] not in y:
          x[j] = None

  print(s)

def dominance(arr):
  print(arr)
  n = len(arr)
  s = []

  t = []
  for i in range(n):
    e = (arr[i][0], arr[i][1], i)
    t.append(e)

  x = sorted(t, key=lambda e: e[0])
  y = [e[1] for e in sorted(t, key=lambda e: e[1])]

  #print(x)
  #print(y)

  for i in range(n):
    t[i] = (x[i][0], y.index(x[i][1]), x[i][2])

  print(t)

  k = float("+inf")
  for i in range(n):
    # "<" Jeżli punkt dominiuje sam siebie tz. "<="
    # "<=" Jeżli punkt nie dominiuje sam siebie tz. "<"
    if t[i][1] <= k:
      s.append(t[i][2])
      k = t[i][1]

  print(s)


