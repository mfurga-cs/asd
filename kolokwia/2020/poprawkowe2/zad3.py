#!/usr/bin/env python3
#
# Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
# jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
# T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
# do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
# wartość -1.
#
# f(i) - minimalny koszt przejścia do i używając liczb 0 ... i.
# f(i) = min(f(j) + |T[i] - T[j]|) jeśli T[i] i T[j] spełniają warunki.
#
# Złożoność: O(n^2)

from zad3testy import runtests

def common_digit(D, i, j):
  for d in range(10):
    if D[i][d] == D[j][d] == 1:
      return True
  return False

def f(F, T, D, i):
  if i == 0:
    return 0

  if F[i] is not None:
    return F[i]

  F[i] = float("+inf")
  for j in range(i):
    if common_digit(D, i, j):
      F[i] = min(F[i], f(F, T, D, j) + abs(T[i] - T[j]))
  return F[i]

def find_cost(T):
  n = len(T)
  # Wyznaczamy min i max i wstawiamy odpowiednio na początek i koniec ciągu.
  mini = min(range(n), key=T.__getitem__)
  maxi = max(range(n), key=T.__getitem__)
  T[0], T[mini] = T[mini], T[0]
  T[n - 1], T[maxi] = T[maxi], T[n - 1]

  D = [[0] * 10 for _ in range(n)]
  for i in range(n):
    num = T[i]
    while num > 0:
      D[i][num % 10] = 1
      num //= 10

  F = [None] * n
  f(F, T, D, n - 1)
  return F[n - 1] if F[n - 1] != float("+inf") else -1

runtests(find_cost)

