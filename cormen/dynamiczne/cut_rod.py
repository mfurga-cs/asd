#!/usr/bin/env python3

def memoized_cut_rod_aux(p, n, r):
  if n == -1:
    return 0
  if r[n] >= 0:
    return r[n]
  q = float("-inf")
  for i in range(n + 1):
    q = max(q, p[i] + memoized_cut_rod_aux(p, n - i - 1, r))
  r[n] = q
  return q

def memoized_cut_rod(p, n):
  r = [float("-inf") for _ in range(n + 1)]
  return memoized_cut_rod_aux(p, n, r)

def cut_rod_(p, n):
  print("cut_rod(%i)" % n)
  if n == -1:
    return 0
  q = float("-inf")
  for i in range(n + 1):
    q = max(q, p[i] + cut_rod(p, n - i - 1))
  return q

def cut_rod(p, n):
  r = [-999 for _ in range(n + 1)]
  r[0] = 0

  for i in range(n + 1):
    q = float("-inf")
    for j in range(i + 1):
      if i - j - 1 == 0:
        q = max(q, p[j])
      else:
        q = max(q, p[j] + r[i - j - 1])
    r[i] = q

  return r[n]

t = [1,5,8,9,10,17,17,20,24,30]

