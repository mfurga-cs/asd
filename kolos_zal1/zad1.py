from zad1testy import runtests

def inorder(l, p):
  if p is None:
    return
  inorder(l, p.left)
  l.append(p)
  inorder(l, p.right)

def ConvertTree(p):
  l = []
  inorder(l, p)
  n = len(l)
  for i in range(n):
    l[i].left = l[2 * i + 1] if 2 * i + 1 < n else None
    l[i].right = l[2 * i + 2] if 2 * i + 2 < n else None
    l[i].parent = l[(i - 1) // 2] if i - 1 >= 0 else None
  return l[0]

runtests( ConvertTree )

