from zad3testy import runtests

def minpow2(n):
  p = 1
  while p <= n:
    p *= 2
  return p // 2

def find(T, c, p):
  if p == 0:
    return T.key
  if c & p == 0:
    return find(T.left, c, p // 2)
  else:
    return find(T.right, c, p // 2)

def maxim(T, C):
  m = -1
  for c in C:
    p = minpow2(c)
    v = find(T, c, p // 2)
    m = max(m, v)
  return m

runtests(maxim)

