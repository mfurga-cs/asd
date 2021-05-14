#!/usr/bin/env python3
# Minimalny koszt przejazdu jeśli na każdej stacji możemy tankować tylko do pełna.
#
# f(i) = min. koszt dotarcia do stacji i pod warunkiem że tankujemy do pełna.

MAX_FUEL = 4

def f(i):
  #if MAX_FUEL >= S[i]:
  #  return S[i] * C[i]
  if i == 0:
    return S[0] * C[0]

  m = float("+inf")
  for k in range(i):
    if S[i] - S[k] <= MAX_FUEL:
      m = min(m, f(k) + (S[i] - S[k]) * C[i])
  return m

S = [2, 3, 5]
C = [15, 100, 10]
t = 7

m = float("+inf")
for i in range(len(S)):
  if t - S[i] <= MAX_FUEL:
    m = min(m, f(i))

print(m)

