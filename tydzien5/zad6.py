#!/usr/bin/env python3
# Mateusz Furga

from tests import runTests

def tspf(F, D, B, i, j):
  # Implementacja taka sama jak na wykładzie. Jedyna różnica to nowa tablica B, która służy do
  # zapamiętywania wyboru k-tego miasta.
  if F[i][j] != float("+inf"):
    return F[i][j]

  if i == j - 1:
    F[j - 1][j] = float("+inf")
    for k in range(j - 1):
      q = tspf(F, D, B, k, j - 1) + D[k][j]
      if q < F[j - 1][j]:
        F[j - 1][j] = q
        B[j - 1][j] = k
  else:
    F[i][j] = tspf(F, D, B, i, j - 1) + D[j - 1][j]
    B[i][j] = j - 1
  return F[i][j]

def build_tour(C, B, i, j, t):
  # Funkcja służąca do odtwarzania najkrótszej trasy przy użyciu tablicy B.
  # W tablicy t przechowywana jest tworzona trasa.
  if i < j:
    # Jeżeli i < j to dodajemy k-ty element na początek budowanej trasy.
    # Będą to miasta które odwiedzimy wcześniej.
    k = B[i][j]
    if k >= 0:
      t.insert(0, C[k][0])
      build_tour(C, B, i, k, t)
  else:
    # Jeżeli i > j to dodajemy k-ty element do końca budowanej trasy.
    # Będą to miasta które odwiedzimy później.
    k = B[j][i]
    if k >= 0:
      t.append(C[k][0])
      build_tour(C, B, k, j, t)

def bitonicTSP(C):
  n = len(C)

  # Sortujemy miasta po X.
  C = sorted(C, key=lambda x: x[1])

  # W tablicy D zapisujemy odległości między miastami.
  D = []
  for i in range(n):
    d = []
    for j in range(n):
      d.append(((C[i][1] - C[j][1]) ** 2 + (C[i][2] - C[j][2]) ** 2) ** (1/2.))
    D.append(d)

  # Tablice F do zapamiętywania policzonych wcześniej wyników.
  F = [[float("+inf")] * n for i in range(n)]
  F[0][1] = D[0][1]

  # Tablica B do odtworzenia trasy.
  B = [[-1] * n for i in range(n)]
  B[0][1] = 0

  # Szukamy najkrótszej trasy.
  tour_len = float("+inf")
  for i in range(n - 1):
    tour_len = min(tour_len, tspf(F, D, B, i, n - 1) + D[i][n - 1])

  # Tablica tour będzie przechowywać tworzoną trasę.
  k1 = B[n - 2][n - 1]
  tour = []
  tour.append(C[n - 1][0])
  tour.append(C[k1][0])
  build_tour(C, B, k1, n - 1, tour)

  print(tour_len, ", ".join(tour))
  return tour

runTests(bitonicTSP)
