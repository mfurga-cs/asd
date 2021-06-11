#!/usr/bin/env python3
#
# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę drzewa, pod
# warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)
#

class Node:
  def __init__(self, value):
    self.value = value
    self.parent = None
    self.left = None
    self.right = None

  def add_left_child(self, node):
    self.left = node
    node.parent = self
    return self.left

  def add_right_child(self, node):
    self.right = node
    node.parent = self
    return self.right

def sum(root):
  s = 0

  v = root
  last = None
  back = False

  while True:
    if root.right == last:
      break

    if not back:
      s += v.value

    if back == False and v.left is not None:
      back = False
      v = v.left
    elif last != v.right and v.right is not None:
      back = False
      v = v.right
    else:
      last = v
      back = True
      v = v.parent

  return s

def print_bst(root):
  if root is None:
    return
  print(root.value)
  print_bst(root.left)
  print_bst(root.right)

if __name__ == "__main__":
  root = Node(12)

  left = root.add_left_child(Node(5))
  right = root.add_right_child(Node(15))

  rright = left.add_right_child(Node(7))

  rright.add_left_child(Node(6))

  #print_bst(root)
  print(sum(root))

