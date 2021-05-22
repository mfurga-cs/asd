#!/usr/bin/env python3
#
# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
# być zarówno dodatnie jak i ujemne):
# n1 + n2 + ... + nk
# Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
# kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
# dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
# najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
# wybiera kolejność dodawań.
# Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2,..., nk (w kolejności w jakiej
# występują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą
# wartość bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań.
#
# Na przykład dla tablicy wejściowej: [1,−5, 2] funkcja powinna zwrócić wartość 3, co odpowiada
# dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
# ----
#
# f(i, j) - największa wartość bezwględna sumowań liczb od i do j.
#
# f(i, j) = min(i <= k < j) { max{ f(i, k), f(k + 1, j), | sum(A[i:k]) + sum(A[k+1:j]) | } }
# f(i, i) = 0

def s(A, i, j):
  return sum(A[i:j + 1])

def result(P, A, i, j):
  if i == j:
    return str(A[i])
  k = P[i][j]
  return "(" + result(P, A, i, k) + result(P, A, k + 1, j) + ")"

def f(F, P, A, i, j):
  if i == j:
    return 0

  if F[i][j] is not None:
    return F[i][j]

  F[i][j] = float("+inf")
  for k in range(i, j):
    v = max(f(F, P, A, i, k), f(F, P, A, k + 1, j), abs(s(A, i, k) + s(A, k + 1, j)))
    if v < F[i][j]:
      F[i][j] = v
      P[i][j] = k
  return F[i][j]

def fwrapper(A):
  n = len(A)
  F = [None] * n
  P = [None] * n

  for i in range(n):
    F[i] = [None] * n
    P[i] = [None] * n

  f(F, P, A, 0, n - 1)
  return result(P, A, 0, n - 1)

A = [10, -7, 7, -8]
#A = [1, -5, 2]
print(fwrapper(A))

