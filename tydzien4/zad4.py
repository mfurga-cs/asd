#!/usr/bin/env python3
# Mateusz Furga

# Funkcja odtwarzająca wszystkie LIS.
def print_result(A, C, i):
  n = len(C[i])
  if n > 0:
    c = 0
    # W C[i] znajdują się indeksy następnych elementów po i-tym.
    # Dla każdego takiego indeksu wypisujemy A[i] i wykonujemy print_result.
    for j in range(n):
      print(A[i], end=" ")
      c += print_result(A, C, C[i][j])
    return c
  else:
    # Jeśli dla i-tego elementu tablica C jest pusta tzn, że jest on ostatnim
    # elementem ciągu. Wypisujemy go i kończymy rekurencje zwracając 1 do sumy ciągów.
    print(A[i])
    return 1

def printAllLIS(A):
  n = len(A)
  F = [1 for i in range(n)]
  C = [[] for i in range(n)]

  # Szukamy najdłuższego ciągu malejącego zaczynając od ostatniego elementu idąc do pierwszego.
  for i in range(n - 1, -1, -1):
    # Zamiast tablicy parentów P będziemy mieć teraz tablicę dzieci C.
    # W C[i] będziemy zapisywać tablicę indeksów elementów po i-tym o największej wartości F[j].
    # Dzięki temu będziemy wstanie wrócić do wszystkich dzieci i-tego elementu.
    c = []
    # Szukamy max F[j] elmentów j = i + 1 do końca dla których A[i] < A[j].
    for j in range(i + 1, n):
      if A[i] < A[j] and F[i] == F[j] + 1:
        c.append(j)
      if A[i] < A[j] and F[i] < F[j] + 1:
        F[i] = F[j] + 1
        c = [j]
    C[i] = c

  # Szukamy indeksów o największym F[i]; będą to pierwsze elementy ciągów.
  indexes = []
  longest = 0
  for i in range(n):
    if F[i] == longest:
      indexes.append(i)
    if F[i] > longest:
      longest = F[i]
      indexes = [i]

  # Dla każdego LIS zaczynającego się na i-tym indeksie szukamy pozostałych
  # elementów przy użyciu funkcji rek. print_result i tablicy dzieci.
  c = 0
  for i in indexes:
    c += print_result(A, C, i)
  return c

