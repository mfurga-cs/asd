from zad2testy import runtests
#
# f(node) - min. wartość zbioru w drzewo zakorzenionym w node która oddziela liści w nim od parenta noda.
#
# f(node) = min(f(node.left) + f(node.right), node.value)   jeśli node.left != None and node.right != None
# f(node) = min(f(node.left, node.value)                    jeśli node.right = None
# f(node) = min(f(node.right, node.value)                   jeśli node.left = None
# f(node) = inf                                             jeśli node = None or node.left = None and node.right = None
#

class BNode:
  def __init__( self, value ):
    self.left = None
    self.right = None
    self.parent = None
    self.value = value

def f(node):
  if node == None:
    return float("+inf")

  if node.left == None and node.right == None:
    return float("+inf")

  if node.left == None:
    return min(f(node.right), node.value)

  if node.right == None:
    return min(f(node.left), node.value)

  v = min(f(node.left) + f(node.right), node.value)
  return v

def cutthetree(T):
  """tu prosze wpisac wlasna implementacje"""
  return f(T.left) + f(T.right)

runtests(cutthetree)


