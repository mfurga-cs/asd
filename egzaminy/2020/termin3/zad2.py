from zad2testy import runtests
#
# f(i) - najdłuższy ciąg klocków kończący się na i-tym używający klocków 0 .. i - 1.
#

def contains(A, B):
  if A[0] >= B[0] and A[1] <= B[1]:
    return True
  return False

def f(A, i):
  if i == 0:
    return 1
  h = 1
  for j in range(i):
    if contains(A[i], A[j]):
      h = max(h, f(A, j) + 1)
  return h

def tower(A):
  n = len(A)
  h = 0
  for j in range(n):
    h = max(h, f(A, j))
  return h

runtests(tower)

