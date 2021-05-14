def modulo(k,n):
    temp = k%n
    return temp

def divide(k,n):
    temp = k//n
    return temp

def counting_sort(A,func):
    x = len(A)
    B = [0]*len(A)
    max_k = 0
    for i in range(len(A)):
        if func(A[i],x) > max_k:
            max_k = func(A[i],x)
    def sub_counting_sort(A,B,k,func):
        x = len(A)
        C = [0]*(k+1) #tablica długości max_k
        for j in range(x): #jeśli wartość występuje zliczamy ją
            C[func(A[j],x)] += 1

        for i in range(1,k+1): #sumujemy popednia i nastepna wartość, aby wiedzieć ile miejsc jest zajętych przed obecną wartością
            C[i] += C[i-1]

        for k in range(x-1,-1,-1):
            B[C[func(A[k],x)]-1] = A[k] #-1 spowodowany różnicą między ostatnim indeksem a długością tablicy
            C[func(A[k],x)] = C[func(A[k],x)] - 1 # ^ przypisujemy na właściwych pozycjach tablicy B wartosci A[k], wartosc C[A[k]] jest zmniejszana bo moga wystepowac te same wartosci, nastepna taka sama wartosc zostanie umieszone na mniejszym o 1 indeksie

    sub_counting_sort(A,B,max_k,func)

    return B

def radix(A):
    B = counting_sort(A,modulo) #tablica posortowana po %
    return counting_sort(B,divide) #tablica posortowana po //

print(radix([11,10,55,32,12512,5125,121,441,523,2,1,0]))



def zad2(tab)
{
    0 0 0 1 3 1 3 2 6
    (0, 3) (1, 2) (3,2) (2,1) (6,1)
    (0, 3) (1, 2)(2,1) (3,2) (6,1)
    0 0 0 1 1 2 3 3 6


}






def partition(arr, lo, hi):
  i = lo
  j = lo
  k = hi
  mid = arr[lo]

  while j <= k:
    if arr[j] < mid:
      arr[i], arr[j] = arr[j], arr[i]
      i += 1
      j += 1
    elif arr[j] > mid:
      arr[j], arr[k] = arr[k], arr[j]
      k -= 1
    else:
      j += 1

  return i - 1, j

def _quicksort(arr, lo, hi):
  if lo < hi:
    i, j = partition(arr, lo, hi)
    _quicksort(arr, lo, i)
    _quicksort(arr, j, hi)

def quicksort(arr):
  return _quicksort(arr, 0, len(arr) - 1)





from random import randint
from math import log, ceil, inf


class Pair:
  def __init__(self, val=inf, cnt=0):
    self.val = val
    self.cnt = cnt


def insertion_sort(A, n, x):
  j = n - 1
  while j >= 0 and A[j].val > x:
    A[j+1].val = A[j].val
    j -= 1
  A[j+1].val = x


def insert(A, n, x):
  flag = (n == 0 or A[-1].val < x)
  A.append(Pair(x, 1))
  if flag:
    return

  insertion_sort(A, n, x)


def bin_search(A, n, x):
  if n == 0:
    return None

  l = c = 0
  r = n - 1
  while l <= r:
    c = (l+r)//2
    if A[c].val < x:
      l = c + 1
    elif A[c].val > x:
      r = c - 1
    else:
      while c > 0 and A[c-1].val == x:
        c -= 1
      break

  if A[c].val != x:
    return None
  return c


def counting_sort(A, n, uniques, _n):
  for i in range(1, _n):
    uniques[i].cnt += uniques[i-1].cnt

  B = [0]*n
  for i in range(n-1, -1, -1):
    j = bin_search(uniques, _n, A[i])
    B[uniques[j].cnt-1] = A[i]
    uniques[j].cnt -= 1

  for i in range(n):
    A[i] = B[i]


def sort_logn_unique_vals(A):
  uniques = []
  _n = 0

  for e in A:
    # log(log(n))
    res = bin_search(uniques, _n, e)
    # log(n) razy (total)
    if res is None:
      insert(uniques, _n, e) # log(n)
      _n += 1
    # n - log(n) razy (total)
    else:
      uniques[res].cnt += 1

























  counting
_sort(A, n, uniques, _n)


n = 100
_n = ceil(log(n, 2))
A = [randint(0, _n) for i in range(n)]
print(A)
sort_logn_unique_vals(A)
print(A)
