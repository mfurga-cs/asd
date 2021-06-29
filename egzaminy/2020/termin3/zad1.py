from zad1testy import runtests
from collections import deque

def bfs(G, s):
  n = len(G)
  visited = [False] * n
  parent = [-1] * n
  distance = [0] * n

  max_vertex = -1
  max_length = float("-inf")

  queue = deque()
  visited[s] = True
  distance[s] = 0

  queue.append(s)
  while len(queue) > 0:
    u = queue.popleft()

    if distance[u] > max_length:
      max_length = distance[u]
      max_vertex = u

    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        distance[v] = distance[u] + 1
        queue.append(v)

  return max_length, max_vertex, parent

def diameter(G):
  _, max_vertex, _ = bfs(G, 0)
  length, v, parent = bfs(G, max_vertex)
  diam = []
  while v != -1:
    diam.append(v)
    v = parent[v]
  return diam, length

def best_root(L):
  diam, length = diameter(L)
  return diam[length // 2]

runtests(best_root)

