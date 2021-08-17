#
# Złożoność: O(n^3)

from zad3testy import runtests

def interselect(a, b):
  if a[1] < b[0] or a[0] > b[1]:
    return None
  return (max(a[0], b[0]), min(a[1], b[1]))

def count_intervals(A, interval):
  n = len(A)
  ints = []
  for i in range(n):
    if A[i][0] <= interval[0] and A[i][1] >= interval[1]:
      ints.append(i)
  return ints

def kintersect(A, k):
  n = len(A)

  max_ints = []
  max_len = 0

  for i in range(n):
    for j in range(n):
      interval = interselect(A[i], A[j])
      if interval is None:
        continue
      interval_len = interval[1] - interval[0]
      if interval_len <= max_len:
        continue
      ints = count_intervals(A, interval)
      if len(ints) >= k:
        max_len = interval_len
        max_ints = ints

  return max_ints

runtests(kintersect)

