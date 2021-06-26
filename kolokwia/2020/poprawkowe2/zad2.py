#
#
#

from zad2testy import runtests
from queue import PriorityQueue

def dijkstra(G, L, W, s):
  n = len(G)
  V = [False] * n

  Q = PriorityQueue()
  Q.put((0, (s, 0, 0)))

  while Q.qsize() > 0:
    _, u = Q.get()
    u, i, d = u

    if i == len(W) - 1:
      return d

    for v, w in G[u]:
      if L[v] != W[i + 1]:
        continue
      Q.put((d + w, (v, i + 1, d + w)))

  return float("+inf")

def letters(G, W):
  L, E = G
  n = len(L)
  G = [[] for _ in range(n)]

  for u, v, w in E:
    G[u].append((v, w))
    G[v].append((u, w))

  v = float("+inf")
  for i in range(n):
    if L[i] == W[0]:
      v = min(v, dijkstra(G, L, W, i))
  return v

runtests(letters)

