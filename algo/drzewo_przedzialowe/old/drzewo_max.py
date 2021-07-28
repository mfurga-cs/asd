#!/usr/bin/env python3
#
# Dany jest ciąg klocków (K1, ..., Kn). Klocek Ki zaczyna sie na pozycji ai i ciągnie
# się do pozycji bi (wszystkie pozycje to nieujemne liczby naturalne) oraz ma wysokość 1. Klocki układane są po
# kolei–jeśli klocek nachodzi na któryś z poprzednich, to jest przymocowywany na szczycie poprzedzającego
# klocka). Na przykład dla klocków o pozycjach (1, 3), (2, 5), (0, 3), (8, 9), (4, 6) powstaje konstrukcja o
# wysokości trzech klocków. Proszę podać możliwie jak najszybszy algorytm, który oblicza wysokośc powstałej
# konstrukcji.
#

from math import ceil, log
from inttree import *

TREE_MAX = []
TREE_LAZY = []

def tree_init(n):
  global TREE_MAX
  global TREE_LAZY
  n = pow(2, ceil(log(n, 2)))
  TREE_MAX = [0] * (2 * n)
  TREE_LAZY = [0] * (2 * n)

def tree_update(p, k, val):
  _tree_update(p, k, 1, 0, len(TREE_MAX) // 2 - 1, val)

def _tree_update(p, k, v, a, b, val):
  if a > k or b < p:
    return

  if a >= p and b <= k:
    TREE_MAX[v] = val
    TREE_LAZY[v] = val
    return

  _tree_lazy_update(v)

  _tree_update(p, k, v * 2, a, (a + b) // 2, val)
  _tree_update(p, k, v * 2 + 1, (a + b) // 2 + 1, b, val)
  TREE_MAX[v] = max(TREE_MAX[v * 2], TREE_MAX[v * 2 + 1])

def tree_max(p, k):
  return _tree_max(p, k, 1, 0, len(TREE_MAX) // 2 - 1)

def _tree_max(p, k, v, a, b):
  # Jeżeli pytany przez nas przedział (p, k) jest rozłączny z przedziałem
  # za który odpowiada dany wierzchołek (a, b) to zwracamy 0 bo to jego to nie dotyczy.
  if a > k or b < p:
    return 0

  # Jeżeli pytany przedział (p, k) w całości zawiera przedział (a, b) to zwracamy
  # największą wartość na daym przedziale.
  if a >= p and b <= k:
    return TREE_MAX[v]

  # Przedziały się przecinają lub przedział pytany (p, k) jest wewnątrz przedziału (a, b).
  # Pytamy dzieci o maksymalny przedział na (p, k).
  _tree_lazy_update(v)

  left = _tree_max(p, k, v * 2, a, (a + b) // 2)
  right = _tree_max(p, k, v * 2 + 1, (a + b) // 2 + 1, b)
  return max(left, right)

def _tree_lazy_update(v):
  if TREE_LAZY[v] == 0:
    return
  # Ustawiamy prawidłowe wartości dla dzieci v.
  TREE_MAX[2 * v] = TREE_LAZY[v]
  TREE_MAX[2 * v + 1] = TREE_LAZY[v]
  # Dzieciom ustawiamy wartości do zamiany na potem.
  TREE_LAZY[2 * v] = TREE_LAZY[v]
  TREE_LAZY[2 * v + 1] = TREE_LAZY[v]
  TREE_LAZY[v] = 0

def main(blocks):
  n = max(blocks)[1]
  tree_init(n)

  for p, k in blocks:
    m = tree_max(p, k)
    tree_update(p, k, m + 1)
    m = tree_max(p, k)

  return tree_max(0, len(TREE_MAX) // 2 - 1)

def main2(blocks):
  points = []
  for b, e in blocks:
    points.append(b)
    points.append(e)

  points = sorted(list(set(points)))
  T = tree(points)
  print(points)

  for p, k in blocks:
    m = tree_maxi(T, (p, k))
    tree_set(T, (p, k), m + 1)

  return tree_maxi(T, (points[0], points[len(points) - 1]))

if __name__ == "__main__":
  blocks = [(1, 3), (2, 5), (0, 3), (8, 9), (4, 6)]
  #blocks = [(1, 2)] * 70

  size = 1000000
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  blocks.append((size, size + size // 2))
  n = len(blocks)
  print(main(blocks))


                                                                        