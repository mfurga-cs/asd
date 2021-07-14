/*
  Drzewo przedziałowe na tablicy i lazy propagation.
  Operacje:
    1. update(a, b, v) - ustawia elementy z przedziału a do b na wartość v.
    2. query(i)        - zwraca wartość danego elementu.

  Muszą zachodzić:
  - Łączność
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

  const int NO_OPT = std::numeric_limits<int>::min();

  int opt(int a, int b) {
    if (b == NO_OPT) {
      return a;
    }
    return b;
  }

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.assign(size * 2, NO_OPT);
  }

  void lazy_propagation(int vertex) {
    array[LEFT(vertex)] = opt(array[LEFT(vertex)], array[vertex]);
    array[RIGHT(vertex)] = opt(array[RIGHT(vertex)], array[vertex]);
    array[vertex] = NO_OPT;
  }

  void update(int a, int b, int value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      array[vertex] = value;
      return;
    }

    lazy_propagation(vertex);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);
  }

  void update(int a, int b, int value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int query(int index, int vertex, int left, int right) {
    if (left == right) {
      return array[vertex];
    }

    lazy_propagation(vertex);

    int res;
    int mid = (left + right) / 2;
    if (index <= mid) {
      res = query(index, LEFT(vertex), left, mid);
    } else {
      res = query(index, RIGHT(vertex), mid + 1, right);
    }

    return res;
  }

  int query(int index) {
    return query(index, 0, 0, size - 1);
  }
};

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  st.update(0, n - 1, 0);

  int op, arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d %d", &arg1, &arg2, &arg3);
      st.update(arg1, arg2 - 1, arg3);
    } else {
      scanf("%d", &arg1);
      printf("%d\n", st.query(arg1));
    }
  }
  return 0;
}

