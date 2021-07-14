/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. update(a, b, v) - ustawia elementy z przedziału a do b na wartość max(A[i], v).
    2. query(i)        - zwraca wartość danego elementu.

  Muszą zachodzić:
  - Łączność
  - Przemienność (jeśli nie jest to musimy użyć lazy propagation)
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<int64_t> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.assign(size * 2, 0);
  }

  void update(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      array[vertex] = std::max(array[vertex], value);
      return;
    }

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);
  }

  void update(int a, int b, int64_t value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int64_t query(int index, int vertex, int left, int right) {
    if (left == right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    int64_t res;
    if (index <= mid) {
      res = query(index, LEFT(vertex), left, mid);
    } else {
      res = query(index, RIGHT(vertex), mid + 1, right);
    }

    return std::max(res, array[vertex]);
  }

  int64_t query(int index) {
    return query(index, 0, 0, size - 1);
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

