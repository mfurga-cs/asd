#
# f(i, p) - min. liczba tankowań by dotrzeć do pola i mająć w zapasie dokładnie p
#           jednostek panliwa.
#

from zad3testy import runtests

def cf(T, visited, i, j):
  n = len(T)
  m = len(T[0])

  visited[i][j] = True
  s = T[i][j]

  if i + 1 < n and visited[i + 1][j] is False and T[i + 1][j] > 0:
    s += cf(T, visited, i + 1, j)

  if i - 1 >= 0 and visited[i - 1][j] is False and T[i - 1][j] > 0:
    s += cf(T, visited, i - 1, j)

  if j - 1 >= 0 and visited[i][j - 1] is False and T[i][j - 1] > 0:
    s += cf(T, visited, i, j - 1)

  if j + 1 < m and visited[i][j + 1] is False and T[i][j + 1] > 0:
    s += cf(T, visited, i, j + 1)

  return s

def count_fuel(T, j):
  n = len(T)
  m = len(T[0])

  visited = [[False] * m for _ in range(n) ]

  if T[0][j] == 0:
    return 0
  return cf(T, visited, 0, j)

def result(P, A, i, y):
  if i == 0:
    return [0]
  j = P[i][y]
  return result(P, A, j, max(y + (i - j) - A[j], 0)) + [i]

def f(F, P, A, i, y):
  if i == 0:
    if y <= 0:
      return 0
    return float("+inf")

  if F[i][y] is not None:
    return F[i][y]

  F[i][y] = float("+inf")
  for j in range(i):
    v = f(F, P, A, j, max(y + (i - j) - A[j], 0))
    if v + 1 < F[i][y]:
      F[i][y] = v + 1
      P[i][y] = j

  return F[i][y]

def fwrapper(A):
  n = len(A)
  F = [None] * n
  P = [None] * n

  maxy = sum(A)
  for i in range(n):
    F[i] = [None] * (maxy + 1)
    P[i] = [None] * (maxy + 1)

  v = f(F, P, A, len(A) - 1, 0)
  return result(P, A, len(A) - 1, 0)

def plan(T):
  n = len(T)
  m = len(T[0])
  stations = []

  s = 0
  for row in T:
    s += sum(row)

  # zliczmy plamy jakie da się osiągnąc z j tego miejsca
  for j in range(n):
    stations.append(count_fuel(T, j))

  return fwrapper(stations)[:-1]

runtests(plan)

