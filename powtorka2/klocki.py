#!/usr/bin/env python3
#
# Dany jest ciąg klocków (a1, b1), ... (an, bn). Każdy klocek zaczyna się na pozycji ai
# i ciągnie się do pozycji bi. Klocki mogą spadać w kolejności takiej jak w ciągu.
# Proszę zaimplementować funkcję tower(A), która wybiera możliwie najdłuższy podciąg klocków
# taki, że spadając tworzą wieżę i żaden klocek nie wystaje poza którykolwiek z wcześniejszych
# klocków. Do funkcji przekazujemy tablicę A zawierającą pozycje klocków ai, bi. Funkcja powinna
# zwrócić maksymalną wysokość wieży jaką można uzyskać w klocków w tablicy A.
#

def lis(A, i):
  v = 0
  for j in range(i):
    if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
      v = max(v, lis(A, j))
  return v + 1

def lis(A):
  dp = [1] * len(A)

  for i in range(len(A)):
    for j in range(i):
      if A[i][0] >= A[j][0] and A[i][1] <= A[j][1]:
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)

A = [(1,4),(0,5),(1,5),(2,6),(2,4)]
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]

print(lis(A))
