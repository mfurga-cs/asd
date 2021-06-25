from zad3testy import runtests
from utils import Heap

class Node:
  def __init__(self, val):
    self.next = None
    self.val = val

def tasks(L):
  n = len(L)
  heap = Heap()

  for i in range(n):
    if L[i] is not None:
      heap.put(L[i].val, L[i])

  head = Node("dummy")
  curr = head

  while len(heap) > 0:
    _, l = heap.get()
    if l.next is not None:
      heap.put(l.next.val, l.next)
    curr.next = l
    curr = curr.next

  return head.next

runtests(tasks)

