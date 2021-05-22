#!/usr/bin/env python3

def cut(p, n):
  if n == 0:
    return 0
  q = float("-inf")
  for i in range(n):
    q = max(q, p[i] + cut(p, n - i))
  return q



