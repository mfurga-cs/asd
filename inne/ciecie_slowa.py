#
# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na co najmniej dwa kawałki,
# tak aby każdy kawałek zawierał co najmniej jedną samogłoskę. Proszę napisać funkcję cutting(s), która
# zwraca liczbę sposobów pocięcia słowa na kawałki.
#

SAMLOGLOSKI = ["a", "e", "i", "o", "u", "y"]

def cutting(s, i, cuts=[]):
  if i == -1:
    print(cuts)
    return 1
  r = 0
  ok = False
  for j in range(i, -1, -1):
    if s[j] in SAMLOGLOSKI:
      ok = True
    if ok:
      r += cutting(s, j - 1, [s[j:i+1]] + cuts)
  return r

s = "student"
s = "ocena"
n = len(s)
print(cutting(s, n - 1))

