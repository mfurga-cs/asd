from zad1testy import runtests

def f(A, i, y):
  if i == 0:
    if y <= 0:
      return 0
    return float("+inf")
  v = float("+inf")
  for j in range(i):
    v = min(v, f(A, j, max(y + (i - j) - A[j], 0)) + 1)
  return v

def zbigniew(A):
  n = len(A)
  return f(A, n - 1, 0)

runtests(zbigniew)

