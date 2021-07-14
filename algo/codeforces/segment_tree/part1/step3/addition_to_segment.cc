/*
  Drzewo przedziałowe na tablicy.

  Operacje:
    - add(a, b, v) - dodaj wartość v na przedziale od a do b.
    - find(i)      - zwraca wartość elementu na indeksie i.

  Możemy to wykonać na zwykłym drzewie przedziałwym bez operacji masowej
  edycji. Dodajemy wartość v na początek na indeksie a i odejmujemy wartość
  v na indeksie b + 1. Natomiast wartość na indeksie i możemy obliczyć sumując
  przedział od 0..i.
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
  std::vector<int64_t> array;

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

  void update(int index, int64_t value, int vertex, int left, int right) {
    if (left == right) {
      array[vertex] += value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      update(index, value, LEFT(vertex), left, mid);
    } else {
      update(index, value, RIGHT(vertex), mid + 1, right);
    }

    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
  }

  void update(int a, int b, int64_t v) {
    update(a, v, 0, 0, size - 1);
    if (b + 1 < size) {
      update(b + 1, -1 * v, 0, 0, size - 1);
    }
  }

  int64_t query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    int64_t l = query(a, b, LEFT(vertex), left, mid);
    int64_t r = query(a, b, RIGHT(vertex), mid + 1, right);
    return l + r;
  }

  int64_t query(int index) {
    return query(0, index, 0, 0, size - 1);
  }

};

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int op, arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d %d", &arg1, &arg2, &arg3);
      st.update(arg1, arg2 - 1, arg3);
    } else {
      scanf("%d", &arg1);
      printf("%lld\n", st.query(arg1));
    }
  }

  return 0;
}

