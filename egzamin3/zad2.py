#
# Drzewo trie trzymające w node ilość napisów, które zaczynają się odpowiednim prefiksem
# na który wskazuje node. W rozwiązaniu szukamy nodów, które są ostatnimi dobrymi tj. mają
# count >= 2 na scieżce od korzenia (dzieci albo nie ist. albo mają wszystkie count < 1).
#

from zad2testy import runtests

class Node:
  def __init__(self):
    self.count = 0
    self.lchild = None
    self.rchild = None

def tree_left(tree):
  if tree.lchild is None:
    tree.lchild = Node()
  return tree.lchild

def tree_right(tree):
  if tree.rchild is None:
    tree.rchild = Node()
  return tree.rchild

def tree_search(tree, pref=''):
  result = []
  ok = True
  if tree.lchild is not None and tree.lchild.count >= 2:
    result += tree_search(tree.lchild, pref + '0')
    ok = False
  if tree.rchild is not None and tree.rchild.count >= 2:
    result += tree_search(tree.rchild, pref + '1')
    ok = False
  if ok:
    return result + [pref]
  return result

def double_prefix(L):
  root = Node()
  for word in L:
    tree = root
    for char in word:
      if char == '0':
        tree = tree_left(tree)
      else:
        tree = tree_right(tree)
      tree.count += 1
  return tree_search(root)

runtests(double_prefix)

