#!/usr/bin/env python3
#
# f(i) - max długość najktótszego elementu spośród wybranych do budowy stringu kończoncego się
#        na i-tym znaku.
#
#
# Można też 

def repr(t, s, i):
  if i == 0:
    return 0

  if i < 0:
    return float("+inf")

  v = float("-inf")
  for k in range(i + 1):
    if s[k:i + 1] in t:
      v = max(v, min(repr(t, s, k - 1), (i - k + 1)))

  return v

def repr(t, s, i):
  if i == 0:
    return 0

  if i < 0:
    return float("+inf")

  v = float("-inf")
  for e in t:
    if e == s[i - len(e) + 1:i + 1]:
      v = max(v, min(repr(t, s, i - len(e)), len(e)))

  return v

t = ["ab", "abab", "ba", "bab", "b"]
s = "ababbab"

