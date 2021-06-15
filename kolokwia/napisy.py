#!/usr/bin/env python3

# Mamy dany ciąg napisów S = (s1, ..., sn) oraz pewien napis t. Wiadomo, że t można zapisać jako
# złączenie pewnej ilości napisów z S (z powtórzeniami). Na przykład dla S = (s1, s2, s3, s4, s5)
# gdzie s1 = ab, s2 = abab, s3 = ba oraz s4 = bab, s5 = b, napis t = ababbab można zapisać, między
# innymi, jako s2s4 lub jako s1s1s3s5. Pierwsza reprezentacja ma ”szerokość” 3 (przez szerokość
# rozumiemy długość najkrótszego si użytego w reprezentacji) a druga 1. Proszę opisać algorytm,
# który mając na wejściu S oraz t znajdzie maksymalną szerokość reprezentacji t.
# Proszę oszacować czas działania algorytmu.
#
# Rozwiązanie:
# f(i) - maksymalna szerkość jaką można uzyskać dla słowa t[0:i]
#
# f(i) = max(0<=j<i){ min{ f(j), i - j + 1} jeżeli t[j:i] in S }
#
# O(n^2) dla hash mapy sprawdzanie czy t[j:i] jest w S.


D = {}

def s(i, j):
  return t[i:j+1]

def f(i):
  if i == -1:
    return float("+inf")
  m = float("-inf")
  for j in range(i + 1):
    if s(j, i) in D:
      m = max(m, min(f(j - 1), i - j + 1))
  return m

if __name__ == "__main__":
  S = ["ab", "abab", "ba", "bab", "b"]
  t = "ababbab"

  for w in S:
    D[w] = 1

  print(f(len(t) - 1))

