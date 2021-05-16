#!/usr/bin/env python3
#
# Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
# jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
# T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
# do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
# wartość -1.
#

def same_digit(i, j):
  for k in range(10):
    if digits[i][k] == digits[j][k] == 1:
      return True
  return False

def f(A, i):
  if i == 0:
    return 0
  v = float("+inf")
  for j in range(i):
    if same_digit(i, j):
      v = min(v, f(A, j)) + (A[i] - A[j])
  return v

def main(T):
  global digits
  T = sorted(T)
  digits = [[0] * 10 for _ in range(len(T))]

  for i in range(len(T)):
    num = T[i]
    while num > 0:
      digits[i][num % 10] = 1
      num //= 10

  print(f(T, len(T) - 1))


T = [123, 890, 688, 587, 257, 246]
digits = []
main(T)



