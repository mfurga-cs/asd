from zad1testy import runtests

# Funkcja zwraca kolejny indeks budynku, który możemy wziąć.
def g(T, i):
  a = T[i][1]
  j = i - 1
  while j >= 0 and T[j][2] >= a:
    j -= 1
  return j

def solution(T, P, i, w):
  if i < 0 or P[i][w] is None:
    return []
  c = P[i][w]
  if c == True:
    return solution(T, P, g(T, i), w - T[i][3]) + [T[i][4]]
  return solution(T, P, i - 1, w)

def f(F, P, T, i, w):
  if w < 0:
    return float("-inf")
  if i < 0:
    return 0

  if F[i][w] is not None:
    return F[i][w]

  v1 = f(F, P, T, g(T, i), w - T[i][3]) + T[i][0] * (T[i][2] - T[i][1])
  v2 = f(F, P, T, i - 1, w)

  F[i][w] = max(v1, v2)
  P[i][w] = v1 >= v2

  return F[i][w]

def select_buildings(T, p):
  n = len(T)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    T[i] = tuple(list(T[i]) + [i])
    F[i] = [None] * (p + 1)
    P[i] = [None] * (p + 1)

  T = sorted( T, key=lambda x: x[1])

  f(F, P, T, n - 1, p)
  return sorted(solution(T, P, n - 1, p))

runtests(select_buildings)

