#!/usr/bin/env python3
#
# Szukamy najkrótszej ścieżki przy użyciu GFS. Liczymy jej długość a następnie usuwamy kolejne krawędzie z najktótszej
# scieżki. Jeżli długość się zwiększy zwracamy usuniętą krawędz.
#

from collections import deque
from zad2testy import runtests

def bfs(G, s, t):
  visited = [False] * len(G)
  parent = [-1] * len(G)
  queue = deque()

  visited[s] = True
  queue.append(s)
  done = False

  while len(queue) > 0 and not done:
    u = queue.popleft()

    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        queue.append(v)
        if v == t:
          done = True

  if done is False:
    return None

  path = []
  v = t
  while parent[v] != -1:
    path.append((parent[v], v))
    v = parent[v]

  return path

def path_len(G, s, t):
  visited = [False] * len(G)
  start = [-1] * len(G)
  queue = deque()

  start[s] = 0
  visited[s] = True
  queue.append(s)

  while len(queue) > 0:
    u = queue.popleft()

    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        start[v] = start[u] + 1
        queue.append(v)
        if v == t:
          return start[v]

  return float("+inf")

def enlarge(G, s, t):
  path = bfs(G, s, t)
  if path is None:
      return None

  shorten_path = len(path)

  for e in path:
    p, v = e
    G[p].remove(v)
    G[v].remove(p)

    path = path_len(G, s, t)

    if path_len(G, s, t) > shorten_path:
      return (p, v)

    G[p].append(v)
    G[v].append(p)

  return None

runtests(enlarge)



