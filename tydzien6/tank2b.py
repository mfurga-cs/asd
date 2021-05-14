#!/usr/bin/env python3
# Minimalny koszt przejazdu jeśli na każdej stacji możemy tankować tylko do pełna.
#
# f(i, l) - min. koszt dotarcia do i mając w zapasie l litrów paliwa.
#
# f(i, l) - min{ f(i - 1, l - 1), f(i - 1, 1) + C[i] }

MAX_FUEL = 3

def tank1(i, n, f, S, C):
  if f < 0:
    return float("+inf")

  if i == n:
    return 0

  v1 = tank1(i + 1, n, f - 1, S, C)
  v2 = float("+inf")
  if i in S:
    v2 = tank1(i + 1, n, MAX_FUEL - 1, S, C) + C[S.index(i)] * (MAX_FUEL - f)
  return min(v1, v2)

def tank3(i, dest, f, S, C):
  if f < 0:
    return float("+inf")

  if i == len(S) - 1:
    if dest - S[i] > f and dest - S[i] > MAX_FUEL:
      return float("+inf")
    elif dest - S[i] > f:
      return C[i] * (MAX_FUEL - f)
    else:
      return 0

  v1 = tank3(i + 1, dest, f - (S[i + 1] - S[i]), S, C)
  v2 = tank3(i + 1, dest, MAX_FUEL - (S[i + 1] - S[i]), S, C) + C[i] * (MAX_FUEL - f)
  return min(v1, v2)

def tank4(i, dest, fuel, S, C):
  if fuel > MAX_FUEL:
    return float("+inf")

  if i == 0:
    print("s[0] + fuel: ", S[0] + fuel)
    # jesteśmy na pierwszej stacji
    if S[0] + fuel <= MAX_FUEL:
      return 0
    else:
      if S[0] + fuel - S[0] <= S[0]:
        return C[0]
      return float("+inf")

  v1 = tank4(i - 1, dest, fuel + (S[i] - S[i - 1]), S, C)
  v2 = tank4(i - 1, dest, (S[i] - S[i - 1]), S, C) + C[i]
  return min(v1, v2)

def tank2(i, f, S, C):
  if i == 0 and f <= MAX_FUEL:
    return 0

  if f > MAX_FUEL:
    return float("+inf")

  k = tank2(i - 1, f + 1, S, C)
  if i in S:
    k = min(k, tank2(i - 1, 1, S, C) + C[S.index(i)] * (f))
  return k

S = [2, 3, 5]
C = [1, 10, 1000]

v = tank1(0, 7, MAX_FUEL, S, C)
print("tank1: ", v)

#v = tank3(0, 7, MAX_FUEL - S[0], S, C)
#print("tank3: ", v)
#v = tank4(len(S) - 1, 7, 0, S, C)
v = tank2(7, 0, S, C)
print("tank4: ", v)

def tank(i, S, C):
  m = float("+inf")
  for l in range(MAX_FUEL):
    m = min(m, tank2(i, l, S, C))
  return m


