from zad3testy import runtests

def get_solution(P, V, i, k):
  if P[i][k] is None:
    return [i]
  ii, kk = P[i][k]
  kk = max(kk, V[ii])
  return get_solution(P, V, ii, kk) + [i]

def f(F, P, T, V, q, i, k):
  if i == 0:
    if k <= V[0]:
      return 0
    return float("+inf")

  # Jeżeli po zatankowaniu mamy mieć więcej niż q to zwracamy inf.
  if k > q:
    return float("+inf")

  # Nie możemy mieć mniej po tankowaniu na i-tej stacji niż V[i].
  if k < V[i]:
    k = V[i]

  if F[i][k] is not None:
    return F[i][k]

  F[i][k] = float("+inf")
  for j in range(i):
    v = f(F, P, T, V, q, j, k + (T[i] - T[j]) - V[i]) + 1
    if v < F[i][k]:
      F[i][k] = v
      P[i][k] = (j, k + (T[i] - T[j]) - V[i])
  return F[i][k]

def iamlate(T, V, q, l):
  T.append(l)
  V.append(0)
  n = len(T)
  m = sum(V)

  F = [None] * (n + 1)
  P = [None] * (n + 1)
  for i in range(n + 1):
    F[i] = [None] * (m + 1)
    P[i] = [None] * (m + 1)

  v = f(F, P, T, V, q, len(T) - 1, 0)

  if v == float("+inf"):
    return []

  i, k = P[len(T) - 1][0]
  v =  get_solution(P, V, i, k)
  return v

runtests( iamlate )

