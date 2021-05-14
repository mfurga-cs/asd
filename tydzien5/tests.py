
def runTests(f):
  c1 = [["Wrocław", 0, 2], ["Warszawa",4,3],["Gdańsk", 2,4], ["Kraków",3,1], ["Paprykarz", 1, 3]]
  p1 = f(c1)
  e1 = ['Wrocław', 'Kraków', 'Warszawa', 'Gdańsk', 'Paprykarz', 'Wrocław']
  print("> TEST 1")
  print("EXCEPT: ", e1)
  print("RESULT: ", p1)
  print()

  assert p1 == e1

  c2 = [
  ("Wrocław", 0, 2),
  ("Sopot", 5, 1),
  ("Gdańsk", 8, 4),
  ("Kraków", 2, 1),
  ("Poznań", 4, 2),
  ("Radom", 3, 4),
  ]

  p2 = f(c2)
  e2 = ['Wrocław', 'Kraków', 'Poznań', 'Sopot', 'Gdańsk', 'Radom', 'Wrocław']
  print("> TEST 2")
  print("EXCEPT: ", e2)
  print("RESULT: ", p2)
  print()

  assert p2 == e2

  c3 = [
  ("Wrocław", 0, 2),
  ("Sopot", 5, 5),
  ("Gdańsk", 8, 4),
  ("Kraków", 2, 0),
  ("Poznań", 4, 6),
  ("Radom", 3, 4),
  ]

  p3 = f(c3)
  e3 = ['Wrocław', 'Radom', 'Poznań', 'Sopot', 'Gdańsk', 'Kraków', 'Wrocław']
  print("> TEST 3")
  print("EXCEPT: ", e3)
  print("RESULT: ", p3)
  print()

  assert p3 == e3

  c4 = [
  ("A", 0, 2),
  ("B", 1, 1),
  ("C", 4, 1),
  ("D", 5, 3),
  ("E", 6, 3),
  ("F", 8, 3),
  ("G", 7, 4),
  ("H", 2, 4),
  ("I", 0.5, 2.5),
  ("J", 1.5, 3.5),
  ]
  
  c4 = [
    ("A", 0, 2),
    ("B", 4, 3),
    ("C", 2, 4),
    ("D", 3, 1),
    ("E", 1, 3),
    ("F", 0.5, -2),
  ]

  p4 = f(c4)
  print(p4)
  return
  e4 = ['Wrocław', 'Radom', 'Poznań', 'Sopot', 'Gdańsk', 'Kraków', 'Wrocław']
  print("> TEST 3")
  print("EXCEPT: ", e3)
  print("RESULT: ", p3)
  print()

  assert p4 == e4







