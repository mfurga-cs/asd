#!/usr/bin/env python3
# Minimalny koszt przejazdu jeśli na każdej stacji możemy tankować tylko do pełna.
#
# f(i, l) - min. koszt dotarcia z i do t mając w zapsasie l litrów paliwa.
#

MAX_FUEL = 3

def tank(i, f):
  if f < 0:
    return float("+inf")

  if i == len(S) - 1:
    if t - S[i] > f and t - S[i] > MAX_FUEL:
      return float("+inf")
    elif t - S[i] > f:
      return C[i] * (MAX_FUEL - f)
    else:
      return 0

  return min(tank(i + 1, f - (S[i + 1] - S[i])),
             tank(i + 1, MAX_FUEL - (S[i + 1] - S[i])) + C[i] * (MAX_FUEL - f))

def tankn(S, C, i):
  if i == 0:
    return S[0] * C[0]
  v = float("+inf")
  for j in range(i):
    if S[i] - S[j] <= MAX_FUEL:
      v = min(v, tankn(S, C, j) + (S[i] - S[j]) * C[i])
  return v

S = [2, 3, 5]
C = [15, 100, 10]

S = [2, 3, 5]
C = [1, 10, 1000]

t = 7

print(tank(0, MAX_FUEL - S[0]))

v = float("+inf")
for i in range(len(S)):
  if t - S[i] <= MAX_FUEL:
    v = min(v, tankn(S, C, i))
print(v)


