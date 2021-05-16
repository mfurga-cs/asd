# Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
# być zarówno dodatnie jak i ujemne):
# n1 + n2 + ... + nk
# Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
# kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
# dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
# najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
# wybiera kolejność dodawań.
# Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość
# bezwzględną wyniku tymczasowego w optymalnej kolejności dodawań. Na przykład dla tablicy
# wejściowej:
# [1,−5, 2]
# funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
# Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji opt sum powinien mieć postać:


def s(A, i, j):
  return sum(A[i:j + 1])

def opt_sum(A, i, j):
  if i == j:
    return 0

  v = float("+inf")
  for k in range(i, j):
    v = min(v, max(opt_sum(A, i, k), opt_sum(A, k + 1, j), abs(s(A, i, k) + s(A, k + 1, j))))

  return v

A = [10, -7, 7, -8]

print(opt_sum(A, 0, len(A) - 1))

