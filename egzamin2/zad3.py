# Mateusz Furga
#
# Drzewo przedziałowe typu przedział-przedział trzymające w node sumę lampek zielonych, czerwonych i niebieskich.
# Po wykonaniu operacji update przesuwamy sumy Z->CZ, CZ->N, N->Z. Dodadkowo w węźle jest trzymana informacja
# ile razy zostało wykonane przesunięcie (modulo 3). Potrzebujemy tej informacji do wykonania operacji update
# dla dzieci w kroku propagacji.
#
# Operacja update polega na przsunięciu sum o jedną pozycję i zwiększeniu count. Złożoność: O(logn).
# Ilość zapalonych lampek niebieskich odczytujemy z korzenia jako sumę niebieskich: Złożoność: O(1).
#
# Złożoność: O(mlogn), Pamięć: O(n)
#

from zad3testy import runtests

class TreeNode:
  def __init__(self, left=None, right=None):
    self.left = left     # Lewy koniec przedziału, za który odpowiada.
    self.right = right   # Prawy koniec przedziału, za który odpowiada.
    self.lchild = None   # Lewe dziecko.
    self.rchild = None   # Prawe dziecko.

    self.green = 1       # Suma zapalonych na zielono.
    self.red = 0         # Suma zapalonych na czerwono.
    self.blue = 0        # Suma zapalonych na niebiesko.
    self.count = 0       # Ile razy wykonano przesunięcie.
    self.lazy = False    # Czy jest liściem. Tzn. czy będziemy wykonowywać propagację.

  def __repr__(self):
    return f"[{self.left}, {self.right}] G={self.green} R={self.red} B={self.blue}"

def _tree_build(points, left, right):
  node = TreeNode(points[left], points[right])
  if left == right:
    return node
  mid = (left + right) // 2
  node.lchild = _tree_build(points, left, mid)
  node.rchild = _tree_build(points, mid + 1, right)
  node.green = node.lchild.green + node.rchild.green
  return node

def tree_build(n):
  points = list(range(n))
  return _tree_build(points, 0, len(points) - 1)

def tree_lazy_propagation(tree):
  if tree.lazy:
    for _ in range(tree.count):
      tree.lchild.red, tree.lchild.blue, tree.lchild.green = tree.lchild.green, tree.lchild.red, tree.lchild.blue

    for _ in range(tree.count):
      tree.rchild.red, tree.rchild.blue, tree.rchild.green = tree.rchild.green, tree.rchild.red, tree.rchild.blue

    tree.lchild.count = (tree.lchild.count + tree.count) % 3
    tree.rchild.count = (tree.rchild.count + tree.count) % 3
    tree.lchild.lazy = True
    tree.rchild.lazy = True

    tree.count = 0
    tree.lazy = False

def tree_update(tree, a, b):
  if tree.right < a or tree.left > b:
    return

  if tree.left >= a and tree.right <= b:
    tree.red, tree.blue, tree.green = tree.green, tree.red, tree.blue
    tree.count = (tree.count + 1) % 3
    tree.lazy = True
    return

  tree_lazy_propagation(tree)

  tree_update(tree.lchild, a, b)
  tree_update(tree.rchild, a, b)

  tree.green = tree.lchild.green + tree.rchild.green
  tree.red = tree.lchild.red + tree.rchild.red
  tree.blue = tree.lchild.blue + tree.rchild.blue

def lamps( n,T ):
  tree = tree_build(n)
  blue_max = 0

  for interval in T:
    tree_update(tree, interval[0], interval[1])
    blue_max = max(blue_max, tree.blue)

  return blue_max

runtests(lamps)

