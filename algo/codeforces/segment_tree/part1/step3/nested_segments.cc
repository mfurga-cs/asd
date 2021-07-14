/*
  Drzewo przedziałwe do zliczania liczby przedziałów zawartych wewnątrz danego,
  reprezentowanych jako ciąg 2n liczb od 1..n gdzie każda występuje dokładnie
  2 razy.
  Algo: Idziemy od lewej prawej. Zapisujemy początki przedziałów do tablicy.
  Jeśli znajdziemy koniec przedziału to sprawdzamy sumę na przedziale od początku
  do końca przedziału. Będzie to liczba przedziałów zawartych w danym. Następnie
  ustawiamy 1 na początku tego przedziału i idziemy dalej.

  Drzewo przedziałowe typu suma i ustaw na idx.
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<int> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.assign(size * 2, 0);
  }

  SegmentTree(int64_t *arr, int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.resize(size * 2);
    for (int i = 0; i < n; i++) {
      array[size - 1 + i] = arr[i];
    }
    build_tree(0, 0, size - 1);
  }

  void build_tree(int vertex, int left, int right) {
    if (left == right) {
      return;
    }
    int mid = (left + right) / 2;
    build_tree(LEFT(vertex), left, mid);
    build_tree(RIGHT(vertex), mid + 1, right);
    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
  }

  void set(int index, int value, int vertex, int left, int right) {
    if (left == right) {
      array[vertex] = value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(index, value, LEFT(vertex), left, mid);
    } else {
      set(index, value, RIGHT(vertex), mid + 1, right);
    }

    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
  }

  void set(int index, int value) {
    set(index, value, 0, 0, size - 1);
  }

  int sum(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    int l = sum(a, b, LEFT(vertex), left, mid);
    int r = sum(a, b, RIGHT(vertex), mid + 1, right);
    return l + r;
  }

  int sum(int a, int b) {
    return sum(a, b, 0, 0, size - 1);
  }

};

int main(void)
{
  int n;
  scanf("%d", &n);
  SegmentTree st(2 * n);
  int pos[n + 1];
  int res[n + 1];

  std::fill_n(pos, n + 1, -1);
  std::fill_n(res, n + 1, 0);

  int v, j;
  for (int i = 0; i < 2 * n; i++) {
    scanf("%d", &v);
    if (pos[v] == -1) {
      pos[v] = i;
    } else {
      j = pos[v];
      res[v] = st.sum(j, i);
      st.set(j, 1);
    }
  }

  for (int i = 1; i <= n; i++) {
    printf("%d ", res[i]);
  }
  printf("\n");

  return 0;
}

