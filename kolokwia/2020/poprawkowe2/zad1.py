#!/usr/bin/env python3
# Złożoność: O(nlogn)
from zad1testy import runtests

# Gdy punkt A słabo dominuję B tj. xa <= xb i ya <= yb.
def dominance(P):
  n = len(P)
  # Sortujemy punkty po X. Jeśli jest kilka o tych samych X to po Y.
  P = [(P[i][0], P[i][1], i) for i in range(n)]
  P = sorted(P)

  # Dodajemy na początek pierwszy punkt o najmniejszym X (i najmniejszym Y). Zawsze musi należeć
  # do zbioru S.
  S = []
  S.append(P[0][2])
  y = P[0][1]

  # Resztę punktów dodajemy tylko wtedy kiedy wsp. Y danego punku jest < od
  # najmniejszej obecnej (y) ze zbioru S.
  i = 1
  while i < n:
    if P[i][1] < y:
      S.append(P[i][2])
      y = P[i][1]
    i += 1

  return S

runtests(dominance)

# Gdy punkt A dominuję B tj. xa < xb i ya < yb.
def dominance(P):
  n = len(P)
  # Sortujemy punkty po X. Jeśli jest kilka o tych samych X to po Y.
  P = [(P[i][0], P[i][1], i) for i in range(n)]
  P = sorted(P)

  # Dodajemy na początek pierwszy punkt o najmniejszym X (i najmniejszej Y). Zawsze musi należeć
  # do zbioru S.
  S = []
  S.append(P[0][2])
  # y - obecnie najmniejsza wsp. po Y punktów ze zbioru S.
  y = P[0][1]
  # y_back - druga w kolejności najmniejsza wsp. po Y punktów ze zbioru S.
  y_back = float("+inf")
  # x - wsp. X punktu, który jest najmniejszy pod względem y w zbiorze S.
  x = P[0][0]

  # Resztę punktów dodajemy tylko wtedy kiedy wsp. Y danego punku jest <= od
  # najmniejszej obecnej (y) ze zbioru S lub kiedy wsp. X danego punktu jest równa
  # wsp. X obecnego najmniejszego punktu ze zbioru S pod względem (y) i jednocześnie
  # wsp Y tego punktu nie jest większa od drugiej najmniejszej po Y ze zbioru S.
  # Jeśli byłaby większa to tamten punkt dominował by dany.
  i = 1
  while i < n:
    if P[i][0] == x and P[i][1] <= y_back:
      S.append(P[i][2])
    if P[i][1] <= y:
      S.append(P[i][2])
      y_back = y
      y = P[i][1]
      x = P[i][0]
    i += 1

  return S

P = [(2, -2), (1, -1), (2.5, -1), (3, 2), (0.5, 3), (0.5, 0.5), (1, 0), (1, 0.6)]
print(dominance(P))

