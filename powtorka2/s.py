#!/usr/bin/env python3

def task(t):
  t = sorted(t, key=lambda v: v[0])
  a = 0
  b = 0

  for i in range(len(t)):
    beg = t[i][0]
    fin = t[i][1]

    if beg >= a:
      a = fin
    elif beg >= b:
      b = fin
    else:
      return "Nope"

  return "ok"

t = [(0, 2), (3, 4), (5, 10), (6, 11), (10, 13), (12, 15), (13, 14)]
print(task(t))


