#!/usr/bin/env python3

def f(s, m):
  if s == 0:
    return 0
  if s < 0:
    return float("+inf")
  res = float("+inf")
  for i in m:
    res = min(res, f(s - i, m))
  return res + 1

