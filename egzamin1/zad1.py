# Mateusz Furga
# Zapisujemy idx elementów do tablicy. Następnie sortujemy stabinie mergesortem.
# Potem sprawdzamy max odchylanie lementów.
#
# Złożoność: O(nlogn)
#

from zad1testy import runtests

def merge(A, C, l, m, r):
  for i in range(l, r + 1):
    C[i] = A[i]

  i, j = l, m + 1

  for k in range(l, r + 1):
    if i > m:
      A[k] = C[j]; j += 1
    elif j > r:
      A[k] = C[i]; i += 1
    elif C[i][0] <= C[j][0]:
      A[k] = C[i]; i += 1
    elif C[i][0] > C[j][0]:
      A[k] = C[j]; j += 1

def _mergesort(A, C, l, r):
  if l < r:
    m = (l + r) // 2
    _mergesort(A, C, l, m)
    _mergesort(A, C, m + 1, r)
    merge(A, C, l, m, r)

def mergesort(A):
  C = A[:]
  return _mergesort(A, C, 0, len(A) - 1)

def chaos_index(T):
  n = len(T)
  for i in range(n):
    T[i] = (T[i], i)
  mergesort(T)
  k = 0
  for i in range(n):
    k = max(k, abs(i - T[i][1]))
  return k

runtests(chaos_index)

