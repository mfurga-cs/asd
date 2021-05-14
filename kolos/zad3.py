# Mateusz Furga
# Tworzumy kubełki zgodnie z przedziałami. Sortujemy w każdym kubełki przy użyciu quicksorta.

# Złożoność czasowa O(nlogn)
# Pamieciowa: O(n)

from zad3testy import runtests

def _partition(a, lo, hi):
  p = a[hi]
  i = lo - 1

  for j in range(lo, hi):
    if a[j] < p:
      i += 1
      a[i], a[j] = a[j], a[i]

  a[i + 1], a[hi] = a[hi], a[i + 1]
  return i + 1

def _quicksort(a, lo, hi):
  if lo < hi:
    j = _partition(a, lo, hi)
    _quicksort(a, lo, j - 1)
    _quicksort(a, j + 1, hi)

def quicksort(a):
  return _quicksort(a, 0, len(a) - 1)

def SortTab(T, P):
  k = len(P)
  n = len(T)

  mn = float("+inf")
  mx = 0
  for i in range(k):
    mn = min(mn, P[i][0])
    mx = max(mx, P[i][1])

  buckets = [[] for _ in range(n)]

  for i in range(n):
    idx = int(((T[i] - mn) / (mx - mn)) * n)
    idx = min(idx, n - 1)
    buckets[idx].append(T[i])

  for i in range(n):
    quicksort(buckets[i])

  i = 0
  for b in buckets:
    for e in b:
      T[i] = e
      i += 1

  return T

P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]

#print(P)
#SortTab( T, P)
runtests( SortTab )

