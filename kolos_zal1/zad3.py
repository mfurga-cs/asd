from zad3testy import runtests

def result(P, T, V, i, y):
  if i == 0:
    return [0]
  j = P[i][y]
  return result(P, T, V, j, max(y + (T[i] - T[j]) - V[j], 0)) + [i]

def f(F, P, T, V, q, i, y):
  if i == 0:
    if y <= 0:
      return 0
    return float("+inf")

  if F[i][y] is not None:
    return F[i][y]

  F[i][y] = float("+inf")
  for j in range(i):
    v = f(F, P, T, V, q, j, max(y + (T[i] - T[j]) - V[j], 0))
    if v + 1 < F[i][y]:
      F[i][y] = v + 1
      P[i][y] = j

  return F[i][y]

def fwrapper(T, V, q):
  n = len(T)
  F = [None] * n
  P = [None] * n

  maxy = sum(V)
  for i in range(n):
    F[i] = [None] * (maxy + 1)
    P[i] = [None] * (maxy + 1)

  v = f(F, P, T, V, q, len(T) - 1, 0)
  return result(P, T, V, len(T) - 1, 0)

def iamlate(T, V, q, l):
  T.append(l)
  V.append(0)
  v = fwrapper(T, V, q)
  return v

runtests( iamlate )

