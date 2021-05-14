#!/usr/bin/env python3
#
# f(i) - czy da się podzielić string na space od 0 do i
#

from collections import defaultdict

def _space(s, d, b, i):
  if i == 0:
    return d[s[i]]
  if i < 0:
    return True
  v = False
  for k in range(i + 1):
    p = d[s[k:i + 1]] and _space(s, d, b, k - 1)
    if p is True:
      v = p
      b[i] = k
  return v

def print_solution(s, b, i):
  if i == 0:
    return s[i]
  if i < 0:
    return ""
  k = b[i]
  return print_solution(s, b, k - 1) + " " + s[k: i + 1]

def space(s, d):
  n = len(s)
  b = [-1] * (n)
  v =_space(s, d, b, n - 1)
  if v:
    print(print_solution(s, b, n - 1)[1:])

def default():
  return False

d = defaultdict(default)
d["ala"] = True
d["ma"] = True
d["kota"] = True
d["mateusz"] = True
d["ewa"] = True
d["lubi"] = True
d["i"] = True
d["nie"] = True
d["psa"] = True
d["kot"] = True

