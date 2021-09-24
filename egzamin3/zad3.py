#
# Złożoność: O(mlogn), Pamięć: O(1)
#

from zad3testy import runtests

def minpow2(n):
  p = 1
  while p <= n:
    p *= 2
  return p // 2

def find(T, c, p):
  while p != 0:
    if c & p == 0:
      T = T.left
    else:
      T = T.right
    p //= 2
  return T.key

def maxim(T, C):
  m = -1
  for c in C:
    p = minpow2(c)
    v = find(T, c, p // 2)
    m = max(m, v)
  return m

runtests(maxim)

