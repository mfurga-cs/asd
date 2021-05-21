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

  if j - 1 >= 0 and visited[i][j - 1] is False and T[i][j - 1] > 0: s += cf(T, visited, i, j - 1)

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

def f(dp, back, A, i, p):
  if i == 0 and p <= A[0]:
    return 0

  if i == 0:
    return float("+inf")

  if p < 0:
    return float("+inf")

  if dp[i][p] is not None:
    return dp[i][p]

  k = float("+inf")
  for j in range(i):
    v = f(dp, back, A, j, p + (i - j) - A[i])
    if v <= k:
      k = v
      back[i] = j

  dp[i][p] = k + 1
  return k + 1

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

  dp = [[None] * (s + 1) for _ in range(m + 1)]
  back = [None] * (m)

  v = f(dp, back, stations, len(stations) - 1, 0)

  print(v)

  l = []
  i = len(stations) - 1

  print(back)

  while back[i] is not None:
    l.insert(0, back[i])
    i = back[i]

  return l

runtests(plan)

