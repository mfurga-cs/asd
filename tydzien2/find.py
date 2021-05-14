

def partition(t, l, h):
  p = t[h]
  i = l - 1

  for j in range(l, h):
    if t[j] < p:
      i += 1
      t[i], t[j] = t[j], t[i]

  t[i + 1], t[h] = t[h], t[i + 1]
  return i + 1

def find(t, i):
  n = len(t)
  l = 0
  h = n - 1

  while True:
    p = partition(t, l, h)

    if p == i:
      return t[p]

    if p > i:
      h = i
    else:
      l = i



