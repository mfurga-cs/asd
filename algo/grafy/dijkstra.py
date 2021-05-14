#!/usr/bin/env python3

from queue import PriorityQueue

def neighbors(v):
  return v

def dijkstra(G, s):
  Q = PriorityQueue()
  S = {}


G = [
  [2, 3],       # 0
  [3, 4],       # 1
  [3, 4],       # 2
  [0],          # 3
  [1]           # 4
]


import heapq
customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))


print(customers)
