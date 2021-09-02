# Mateusz Furga
#
# W korzeniu drzewa zapisujemy informację:
#   T.sum - suma wag w drzewie wejściowym.
#   T.diff - min. różnica drzew.
#   T.edge - id wierzchołka, dla którego T.diff jest najmniejsze.
#
# Usuwamy każdą krawędź idąc alg. DFS po drzewie. Po każdym usunięciu krawędzi liczymy
# sumę wag drzewa dostępnego z korzenia i obliczamy wagę drugiego jako
# T.sum - (usunięta krawędź) - (waga drzewa z korzenia).
# Poprawiamy T.diff jeśli różnica wag drzew jest mniejsza i zapisujemy T.edge.
#
# Złożoność: O(n^2), Pamięć: O(1 + ramki stosu dla rekurencji)
#

from zad2testy import runtests

# Python nie widział klasy Node z pliku.
class Node:
  def __init__( self ):   # stwórz węzeł drzewa
    self.edges   = []     # lista węzłów do których są krawędzie
    self.weights = []     # lista wag krawędzi
    self.ids     = []     # lista identyfikatorów krawędzi

  def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
    self.edges.append( x )       # o wadze w i identyfikatorze id
    self.weights.append( w ) 
    self.ids.append( id )

  def __str__( self ):
    s = "["
    for i in range(len(self.edges)):
      s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
      s += ","
    s+= "]"
    return s

def tree_sum(node):
  if node is None:
    return 0
  s = 0
  for e in node.edges:
    s += tree_sum(e)
  for w in node.weights:
    if w == -1:
      continue
    s += w
  return s

def tree_dfs(node, root):
  for i in range(len(node.weights)):
    w = node.weights[i]
    edge = node.edges[i]
    id = node.ids[i]

    # Usuwamy krawędź.
    node.weights[i] = -1
    node.edges[i] = None

    # Liczymy sumy drzew.
    sum1 = tree_sum(root)
    sum2 = root.sum - w - sum1
    if root.diff > abs(sum1 - sum2):
      root.diff = abs(sum1 - sum2)
      root.edge = id

    # Dodajemy usuniętą krawędź.
    node.weights[i] = w
    node.edges[i] = edge

    tree_dfs(edge, root)

def balance(T):
  T.sum = tree_sum(T)
  T.diff = float("+inf")
  T.edge = -1
  tree_dfs(T, T)
  return T.edge

runtests(balance)

