# Mateusz Furga
#
# f(i, k) = maksymalne przecięcie k przedziałów kończące na i-tym używające przedziały od 0..i.
# Funkcja f zwraca maksymalny przeciety przedział.
#
# f(i, k) = max_po_przecięciu(f(j, k - 1))
# Złożoność: O(n * k)

from zad3testy import runtests

def select(A, B):
  if B[0] > A[1] or A[0] > B[1]:
    return None
  s = max(A[0], B[0])
  e = min(A[1], B[1])
  return (s, e)

def len_int(A):
  return A[1] - A[0]

def result(P, A, i, k):
  if k == 1:
    return [i]
  j = P[i][k]
  return result(P, A, j, k - 1) + [i]

def f(F, P, A, i, k):
  if k == 1:
    return A[i]

  if F[i][k] != float("+inf"):
    return F[i][k]

  F[i][k] = None
  for j in range(i):
    B = f(F, P, A, j, k - 1)
    if B is None:
      continue

    R = select(A[i], B)
    if R == None:
      continue

    if R[0] == R[1]:
      continue

    if F[i][k] is None or len_int(R) > len_int(F[i][k]):
      F[i][k] = R
      P[i][k] = j

  return F[i][k]

def kintersect(A, k):
  n = len(A)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    F[i] = [float("+inf")] * (k + 1)
    P[i] = [None] * (k + 1)

  max_idx = -1
  res = None
  for i in range(k - 1, n):
    B = f(F, P, A, i, k)
    if B is None:
      continue
    if res is None or len_int(B) > len_int(res):
      res = B
      max_idx = i

  return result(P, A, max_idx, k)

runtests(kintersect)


