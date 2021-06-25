#!/usr/bin/env python3

def tgf_conv(desc, directed=False):
  """
  TGF converter to matrix reprezentation. Assume verteces are labed from 0 to n.
  """
  G = None
  vertices = 0
  phaze = 0
  for line in desc.strip().splitlines():
    if line == "#":
      G = [[0] * vertices for _ in range(vertices)]
      phaze = 1
      continue
    if phaze == 0:
      vertices += 1
    if phaze == 1:
      u, v, w = map(int, (line.split() + [1])[:3])
      G[u][v] = w
      if directed:
        G[v][u] = w
  return G

