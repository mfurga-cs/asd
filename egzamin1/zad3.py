# Złożoność: O(nlogn + nlogk)

from zad3testy import runtests
from queue import PriorityQueue

def queue_all(q):
  items = []
  while q.qsize() > 0:
    _, item = q.get()
    items.append(item)
  for item in items:
    q.put((item[1], item))
  return items

def kintersect(A, k):
  n = len(A)
  for i in range(n):
    A[i] = (A[i][0], A[i][1], i)

  if k == 1:
    max_interval_len = 0
    max_inerval = None

    for i in range(n):
      if A[i][1] - A[i][0] > max_interval_len:
        max_interval_len = A[i][1] - A[i][0]
        max_inerval = [i]

    return max_inerval

  A = sorted(A)
  q = PriorityQueue()

  max_intersection = []
  max_intersection_len = 0

  for i in range(n):
    if q.qsize() + 1 < k:
      q.put((A[i][1], A[i]))
      continue

    _, first = q.get()

    if min(A[i][1], first[1]) - A[i][0] > max_intersection_len:
      max_intersection_len = min(A[i][1], first[1]) - A[i][0]
      max_intersection = queue_all(q) + [first]
      max_intersection.append(A[i])

    if first[1] < A[i][1]:
      q.put((A[i][1], A[i]))
    else:
      q.put((first[1], first))

  res = []
  for item in max_intersection:
    res.append(item[2])

  return sorted(res)

A = [(0,4),(1,10),(6,7), (2,8)]
k = 3
#kintersect(A, k)

runtests(kintersect)

