#!/usr/bin/env python3

from random import randint, seed

class Node:
  def __init__(self):
    self.next = None
    self.value = None

def partition(head, tail):
  tailnext = tail.next
  pivot = tail
  curr = head

  prev = None
  head = None

  while curr != pivot:
    if curr.value < pivot.value:
      if head is None:
        head = curr
      else:
        prev.next = curr
      prev = curr
    else:
      tail.next = curr
      tail = tail.next

    curr = curr.next

  tail.next = tailnext

  if head is not None:
    prev.next = pivot
  else:
    head = pivot

  return head, prev, pivot, tail

def quicksort(head, tail):
  head, prev, pivot, tail = partition(head, tail)

  if head != pivot:
    head = quicksort(head, prev)

  if pivot != tail:
    pivot.next = quicksort(pivot.next, tail)

  return head

def qsort(head):
  tail = head
  while tail.next is not None:
    tail = tail.next
  return quicksort(head, tail)

def tab2list( A ):
  H = Node()
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H.next

def printlist( L ):
  while L != None:
    print( L.value, "->", end=" ")
    L = L.next
  print("|")

seed(42)

n = 10
T = [ randint(1,10) for i in range(n) ]
L = tab2list( T )

print("przed sortowaniem: L =", end=" ")
printlist(L) 
L = qsort(L)
print("po sortowaniu    : L =", end=" ")
printlist(L)

if L == None:
  print("List jest pusta, a nie powinna!")
  exit(0)

P = L
while P.next != None:
  if P.value > P.next.value:
    print("Błąd sortowania")
    exit(0)
  P = P.next

print("OK")

