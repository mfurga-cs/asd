#!/usr/bin/env python3
#
# g(v) - maksymalne skojarzenie w poddrzewie zakorzenionym w v takie że, nie bierzemy krawędzi
#        prowadzących do dzieci z wierzchołka v.
#
# f(v) - maksymalne skojarzenie w poddrzewie zakorzenionym w v takie że, wybieramy co najwyżej
#        1 krawędź prowadzącą do dzieci wierzchołka z v. (Nie możemy więcej bo dostalibyśmy
#        krawędzie mające ten sam wierzchołek).
#
# g(v) = sum{ f(v) }  # Sumujemy podrzewa nie biorąc wag krawędzi prowadzących do podrzew.
# f(v) = g(v) + max{ max{ w(v, u) + g(u) - f(u) }, 0 }
#
#        Na początek sumujemy podrzewa v, czyli nie bierzemy na razie żadnej krawędzi.
#        Następnie rozważamy czy dostaniemy większe skojarzenie jeśli weźniemy krawędz
#        z wierzchołka v lub 0 jeśli się nie opłaca się jej brać bo będzie < 0. Przy dodawaniu
#        krawędzi będziemy "zamieniać" ogarniczenie z f(u) na g(u) dla danej krawędzi prowadzącej
#        do wierzchołka u, ponieważ f(u) nie zakłada że w nie weźniemy następnych krawędzi.
#        Robimy to przez dodawanie g(u) i usuwanie f(u) (bo dodaliśmy je wcześniej w g(v)).
#

class Node(object):
  def __init__(self):
    self.children = []
    self.f = None
    self.g = None

  def __repr__(self):
    return "f=%s g=%s used=%s" % (self.f, self.g, self.used)

  def add_child(self, child, w):
    self.children.append((child, w))

def g(v):
  if v.g is not None:
    return v.g
  v.g = 0
  for u, w in v.children:
    v.g += f(u)
    u.used = False
  return v.g

def f(v):
  if v.f is not None:
    return v.f
  v.f = g(v)
  m = 0
  for u, w in v.children:
    m = max(m, w + g(u) - f(u))
  v.f += m
  return v.f

  """
  Ewentulanie możemy wybierać na początku krawędz i sumować bez tego wierzchołka ale
  mamy 2 fory zagnieżdzone:

  v.f = g(v)
  for u, w in v.children:
    s = 0
    for uu, ww in v.children:
      if uu != u:
        s += f(uu)
    v.f = max(v.f, w + g(u) + s)
  return v.f
  """

if __name__ == "__main__":
  root = Node()
  v1 = Node()
  v2 = Node()
  v3 = Node()

  root.add_child(v1, 10)
  root.add_child(v2, 9)
  root.add_child(v3, 19)

  v4 = Node()
  v5 = Node()
  v6 = Node()
  v7 = Node()
  v8 = Node()
  v9 = Node()

  v1.add_child(v4, 12)
  v1.add_child(v5, 3)
  v1.add_child(v6, 7)

  v3.add_child(v7, 7)
  v3.add_child(v8, 9)
  v3.add_child(v9, 3)

  print(f(root))
  print("-----")


