# Złożoność: O(n^2)

from zad3testy import runtests

def kintersect(A, k):
  n = len(A)
  for i in range(n):
    A[i] = A[i] + (i,)
  A = sorted(A)

  max_len = 0
  max_int = []

  for i in range(n):
    a = A[i]
    counter = 0
    intervals = []

    for j in range(n):
      b = A[j]
      if b[1] < a[1]:
        continue
      if b[0] >= a[1]:
        break

      counter += 1
      intervals.append(b[2])
      if counter == k:
        if max_len < a[1] - b[0]:
          max_len = a[1] - b[0]
          max_int = intervals
        break

  #print(max_int)
  return max_int

A = [(0,4),(1,10),(6,7), (2,8), (4, 6)]
k = 3
kintersect(A, k)

runtests(kintersect)

