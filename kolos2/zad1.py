#
# f(i, p, s) - najwięszky zysk jaki można uzyskać wybierając przedmioty od 0 ... do i nie przekraczając
#              ceny p i tak aby nie zachociły na siebie. S służy do zapamietywanie wybranych przedmiotów.
#

from zad1testy import runtests

def is_valid(s, i):
  h, a, b, w = T[i][0], T[i][1], T[i][2], T[i][3]
  for j in s:
    _, aa, bb, _ = T[j][0], T[j][1], T[j][2], T[j][3]
    if aa < a < bb or aa < b < bb or (a < aa and b > bb):
      return False
  return True

def get_solution(dp, T, i, j):
  if j == 0:
    return []
  if i == 0:
    if dp[i][j] is not None:
      return [i]
    return []
  v1 = dp[i - 1][j]
  v2 = float("+inf")
  if j - T[i][3] >= 0:
    v2 = dp[i - 1][j - T[i][3]] + T[i][0] * (T[i][2] - T[i][1])
  if v1 <= v2:
    return get_solution(dp, T,  i - 1, j)
  return get_solution(dp, T, i - 1, j - T[i][3]) + [i]

def f(dp, T, i, p, s=[]):
  if i < 0:
    return 0

  h, a, b, w = T[i][0], T[i][1], T[i][2], T[i][3]

  if w > p:
    dp[i][p] = f(dp, T, i - 1, p, s)
    return dp[i][p]

  v1 = v2 = f(dp, T, i - 1, p, s)
  if is_valid(s, i):
    v2 = f(dp, T, i - 1, p - w, s + [i]) + (h * (b - a))

  if v1 > v2:
    dp[i][p] = v1
  else:
    dp[i][p] = v2

  return dp[i][p]

def select_buildings(T, p):
  n = len(T)
  dp = [[None for j in range(p + 1)] for i in range(n + 1)]

  #for i in range(n + 1):
  #  dp.append([[None for j in range(n + 1)] for i in range(p + 1)])

  res = f(dp, T, len(T) - 1, p)

  print(res)

  print(get_solution(dp, T, len(T) - 1, p))


T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5


#runtests(select_buildings)
print(select_buildings(T, p))


