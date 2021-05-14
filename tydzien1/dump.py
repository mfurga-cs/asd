# Dump 08.03.2021

class Node():
    def __init__(self, val, next):
        self.val = val
        self.next = next


def print_list(p):
    arr = []
    while p is not None:
        arr.append(p.val)
        p = p.next
    print(arr)

def list_to_node(l):
    head = Node(None, None)
    current = head
    for el in l:
        current.next = Node(el, None)
        current = current.next
    return head
    

def merge(p1, p2):
  head = p1
  prev1 = p1
  p1 = p1.next
  p2 = p2.next
  # Wstawiamy z p2 do p1
  while p2 is not None:
      while p1 is not None and p1.val < p2.val:    
          prev1 = p1
          p1 = p1.next

      
      prev1.next = p2
      temp = p2.next
      p2.next = p1
      p2 = temp
      prev1 = prev1.next
  
  return head
      

def find(head):
  prev = head
  curr = head.next

  while curr is not None and prev.val < curr.val:
    prev = curr
    curr = curr.next
  
  return prev

def mergesort(l):
  curr = l

  while True:
    ser1 = find(curr)
    if ser1.next is None:
      if curr is l:
        return l
      else:
        curr = l
        continue

    ser2 = find(ser1.next)

    merged = merge(curr, ser1)

    if ser2.next is None:
      if curr is l:
        return merged
      else:
        curr = ser2.next
              

# s1 s2 s3 s4 ..
# merged s3 s4 ..  


      

# print_list(
#         merge(
#             list_to_node([1, 10, 100, 101]),
#             list_to_node([0, 11, 12, 99, 100, 102])
#         )
#     )

# print_list(
#         merge(
#             list_to_node([1,4]),
#             list_to_node([-1, 2])
#         )
#     )
# print_list(
#         mergesort(
#           list_to_node([1, 10, 100, 101] + [0, 11, 12, 99, 100, 102])
#         )
#     )
    
licznik = 0
def mergesort(T):
    global licznik
    if len(T) > 1: # warunek końcowy rekurencji - po podzieleniu zostaje jeden element

        srodek = len(T) // 2 # dzielę tablicę na dwie, niekoniecznie równe części
        L = T[:srodek]
        P = T[srodek:]      # powstają dwie tablice - lewa ozn L i prawa ozn P
        mergesort(L)   #sortuje obie tablice rekurencyjnie
        mergesort(P)

        i = j = k = 0 #i,j,k - ozn. indeksy tablic kolejno lewej, prawej oraz wejściowej tablicy

        while i < len(L) and j < len(P):

            if L[i] < P[j]:
                T[k] = L[i]
                i += 1      # posortowane tablice - lewą i prawą - łączę ze sobą tak, aby tablica złożona z połączonych
                            # tych dwóch tablic również była posortowana
            else:
                T[k] = P[j]
                licznik += srodek - i
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1     # jeśli na którejś z tablic skończą się elementy, to do końca przepisuje już elementy z tej
                        # drugiej tablicy
        while j < len(P):
            T[k] = P[j]
            j += 1
            k += 1

    return T

# mergesort([3,2,1,0,5])
# print(licznik)



def sum_below(pts, y):
  _sum = 0
  cnt = 0
  for p in pts:
    if p[0][1] <= y:
      _sum += (p[1][0]-p[0][0])*(p[0][1]-p[1][1])
      cnt += 1

  return (_sum, cnt)


P = 10**2
pts = [((1, 10), (3, 8)), ((2, 10), (3, 6))]

y_prev = -1
y = pts[0][0][1]
e = 0.1
while abs(y - y_prev) > e:
  res = sum_below(pts, y)
  if res[0] < P:
    y_prev, y = y, 1.5*y
  else:
    y_prev, y = y, 0.5*y

print(res[1])