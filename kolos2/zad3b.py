#
# Rozwiązanie zachłanne. Wybieramy max.
#

from zad3testy import runtests
from queue import PriorityQueue

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

def min_stops(A):
  n = len(A)
  scope = 0
  count = 0

  V = [False] * n

  q = PriorityQueue()
  q.put((A[0], (0, A[0])))
  V[0] = True

  res = []

  while True:
    _, v = q.get()
    i, v = v

    res.append(i)

    scope += v
    count += 1

    for i in range(scope + 1):
      if i == len(A) - 1:
        return res

      if V[i]:
        continue
      V[i] = True

      q.put((A[i] * -1, (i, A[i])))

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

  return min_stops(stations)

runtests(plan)

