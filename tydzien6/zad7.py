#!/usr/bin/env python3
# Mateusz Furga

from queue import PriorityQueue

# Klasa reprezentująca element w drzewie binarnym.
class Node:
  def __init__(self, val, idx, left=None, right=None):
    self.val = val      # Znak.
    self.idx = idx      # Indeks znaku w tablicy S.
    self.left = left
    self.right = right

  def __lt__(self, other):
    pass

# Rekurencja do przechodzenia po drzewie binarnym. W p tworzony jest kod
# zgodnie z tym czy idziemy do lewego lub prawego dziecka. Funkcja zwraca wartość
# drzewa jako sumę iloczynów częstości i długości kodów.
def gen(node, C, p=""):
  if node is None:
    return 0
  if node.val is not None:
    C[node.idx] = p
    return F[node.idx] * len(p)
  return gen(node.left, C, p + "0") + gen(node.right, C, p + "1")

def huffman(S, F):
  n = len(S)
  # Tablica C do przechowywania utworzonych kodów dla znaków.
  C = [None] * n

  queue = PriorityQueue()

  # Dodajemy do kolejki elementy z S jako obiekty Node.
  for i in range(n):
    queue.put((F[i], Node(S[i], i)))

  # Tworzymy drzewo binarne zdejmując 2 elementy o najmniejszej częstości.
  # Sumujemy ich częstości i dodajemy do kolejki jako nowy node z wartością None.
  while queue.qsize() > 1:
    fa, a = queue.get()
    fb, b = queue.get()
    queue.put((fa + fb, Node(None, None, a, b)))

  # Ostatnim elementem w kolejce jest root drzewa binarnego. Generujemy kody zgodnie
  # z algorytmem Huffmana.
  _, tree = queue.get()
  bits = gen(tree, C)

  for i in range(n):
    print("%s: %s" % (S[i], C[i]))
  print(bits)

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]

S = "matiii"
F = [0] * 256

for c in S:
  F[ord(c)] += 1

F = [i for i in F if i != 0]
S = sorted("".join(set(S)))

print(S)
print(F)

huffman(S, F)

