#!/usr/bin/env python3

from collections import deque

class Graph(object):
  def __init__(self, vertices):
    self.vertices = [[] for _ in range(len(vertices))]
    self.n = len(vertices)

  def add_edge(self, v, u):
    self.vertices[v].append(u)

  def remove_edge(self, v, u):
    self.vertices[v].remove(u)

  def neighbors(self, v):
    return self.vertices[v]

  def bfs(self, s):
    visited = [False] * self.n
    parent = [None] * self.n
    distance = [float("+inf")] * self.n

    visited[s] = True
    distance[s] = 0

    Q = deque()
    Q.append(s)
    while len(Q) > 0:
      u = Q.popleft()
      for v in self.neighbors(u):
        if not visited[v]:
          visited[v] = True
          parent[v] = u
          distance[v] = distance[u] + 1
          Q.append(v)

    for i, v in enumerate(distance):
      print(i, ": ", v)

  def dfs_visit(self, u):
    self.time += 1

    self.visited[u] = True
    self.started[u] = self.time

    for v in self.neighbors(u):
      if not self.visited[v]:
        self.parent[v] = u
        self.dfs_visit(v)

    self.time += 1
    self.finished[u] = self.time

  def dfs(self, s):
    self.visited = [False] * self.n
    self.parent = [None] * self.n
    self.started = [-1] * self.n
    self.finished = [-1] * self.n

    self.time = 0
    #for v in range(self.n):
    #  if not self.visited[v]:
    #    self.dfs_visit(v)
    self.dfs_visit(s)

v = [0,1,2,3,4,5,6,7]
g = Graph(v)

g.add_edge(0, 1)
g.add_edge(0, 4)

g.add_edge(1, 0)
g.add_edge(1, 5)

g.add_edge(2, 5)
g.add_edge(2, 6)
g.add_edge(2, 3)

g.add_edge(3, 2)
g.add_edge(3, 6)
g.add_edge(3, 7)

g.add_edge(4, 0)

g.add_edge(5, 1)
g.add_edge(5, 2)
g.add_edge(5, 6)

g.add_edge(6, 5)
g.add_edge(6, 2)
g.add_edge(6, 3)
g.add_edge(6, 7)

g.add_edge(7, 6)
g.add_edge(7, 3)

g.dfs(1)

#g.print()

