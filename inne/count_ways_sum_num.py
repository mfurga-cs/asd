#!/usr/bin/env python3

def sum(A, s, nums=[]):
  if s < 0:
    return 0
  if s == 0:
    print(nums)
    return 1
  c = 0
  for n in A:
    c += sum(A, s - n, nums + [n])
  return c

# Bez powtarzania. Sortujemy listę liczb i pamiętam ostanio wybraną.
# Potem przechodzimy tylko od niej do większych.
def sum2(A, s, i, nums=[]):
  if s < 0:
    return 0
  if s == 0:
    print(nums)
    return 1
  if i >= len(A):
    return 0
  c = 0
  c += sum2(A, s - A[i], i, nums + [A[i]])
  c += sum2(A, s, i + 1, nums)
  return c

A = [1,2,3]
s = 4
#print(sum(A, s))
print(sum2(A, s, 0))


