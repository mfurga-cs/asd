#!/usr/bin/env python3

from collections import deque

def neighbors(v):
  return v

def BFS(G, s):
  V = [False] * len(G)   # Visited
  P = [-1] * len(G)      # Parent

  V[s] = True
  P[s] = -1

  Q = deque()
  Q.append(s)

  while len(Q) > 0:
    u = Q.popleft()
    for v in neighbors(G[u]):
      if not V[v]:
        print(v)
        V[v] = True
        P[v] = u
        Q.append(v)

def DFS(G, s):
  V = [False] * len(G)   # Visited
  P = [-1] * len(G)      # Parent
  S = [-1] * len(G)      # Start time
  F = [-1] * len(G)      # Finished time

  time = 0

  def DFS_visit(u):
    nonlocal time
    time += 1

    print(u)
    V[u] = True
    S[u] = time

    for v in neighbors(G[u]):
      if not V[v]:
        P[v] = u
        DFS_visit(v)

    time += 1
    F[u] = time

  DFS_visit(s)

G = [
  [2, 3],       # 0
  [3, 4],       # 1
  [3, 4],       # 2
  [0],          # 3
  [1]           # 4
]

DFS(G, 0)

