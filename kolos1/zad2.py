# Mateusz Furga
# Wkładamy pierwsze k + 1 elementów do min-heap. Przechodzimy po liście zdejmując element z minheap i dodajemy
# go do nowo powstałej listy. Kolejny element dodajemy do minheap.
#
# Zlozoność algorytmu nlog(k)
#
# Dla k = O(1) O(n)
# dla k = O(logn) O(nloglogn)
# dla k = O(n) O(nlogn)

from zad2testy import runtests
from utils import *

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

def print_list(l):
  while l is not None:
    print(l.val, end=" -> ")
    l = l.next
  print("None")

def SortH(p, k):
  heap = Heap()

  for i in range(k + 1):
    heap.put(p.val, p)
    p = p.next

  head = Node("dummy")
  curr = head

  while p is not None:
    _, node = heap.get()
    curr.next = node
    curr = curr.next

    heap.put(p.val, p)
    p = p.next

  while len(heap) > 0:
    _, node = heap.get()
    curr.next = node
    curr = curr.next

  curr.next = None
  return head.next

runtests(SortH)

