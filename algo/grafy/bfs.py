#!/usr/bin/env python3

from collections import deque

def bfs(G, s):
  visited = [False] * len(G)
  parent = [-1] * len(G)
  queue = deque()

  visited[s] = True
  queue.append(s)

  while len(queue) > 0:
    u = queue.popleft()

    # do whatever
    print(u)

    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)

G = [
  [1, 4],
  [0, 2],
  [1, 3],
  [2, 4],
  [0, 3]
]

bfs(G, 0)

