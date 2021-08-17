#!/usr/bin/env python3
#
# Szukamy przedziału, który zawiera jak najwięcej innych przedziałów.
#

def max_inclusion(I):
  C = I[:]
  n = len(I)

  for i in range(n):
    I[i] = (I[i][0], I[i][1], i)

  I = sorted(I, key=lambda x: (x[0], -1 * x[1], x[2]))

  # Przedziały, które kończą się przed końcem i-tego przedziału.
  f = [0] * n
  # Przedziały, które zaczynają się przed początkiem i-tego przedziału.
  g = [0] * n

  for i in range(n):
    g[I[i][2]] = i

  I = sorted(I, key=lambda x: (x[1], -1 * x[0], -1 * x[2]))

  for i in range(n):
    f[I[i][2]] = i

  max_inclusion = 0
  max_interval = None

  for i in range(n):
    print(C[i], f[i] - g[i])
    if (f[i] - g[i]) > max_inclusion:
      max_inclusion = f[i] - g[i]
      max_interval = i

I = [(1, 4), (2, 7), (3, 4), (7, 10), (5, 8), (4, 5), (1, 8), (2, 10)]
I = [(2,3),(1,4),(0,5)]
max_inclusion(I)


