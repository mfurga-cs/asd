/*
  Drzewo przedziałowe.

  - update(a, b, v) - dodaje do elementów z przedziału od a do b wartość v.
  - query(x, l)     - zwraca indeks >= l pierwszego wystąpienia liczby >= x.
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
  std::vector<int64_t> max;
  std::vector<int64_t> sum;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    max.assign(size * 2, 0);
    sum.assign(size * 2, 0);
  }

  void lazy_propagation(int vertex) {
    sum[LEFT(vertex)] += sum[vertex];
    sum[RIGHT(vertex)] += sum[vertex];
    max[LEFT(vertex)] += sum[vertex];
    max[RIGHT(vertex)] += sum[vertex];
    sum[vertex] = 0;
  }

  void update(int a, int b, int value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      sum[vertex] += value;
      max[vertex] += value;
      return;
    }

    lazy_propagation(vertex);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    max[vertex] = std::max(max[LEFT(vertex)], max[RIGHT(vertex)]);
  }

  void update(int a, int b, int value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int query(int x, int l, int vertex, int left, int right) {
    if (right < l) {
      return -1;
    }

    if (max[vertex] < x) {
      return -1;
    }

    if (left == right) {
      return left;
    }

    lazy_propagation(vertex);

    int mid = (left + right) / 2;
    int val = query(x, l, LEFT(vertex), left, mid);
    if (val == -1) {
      val = query(x, l, RIGHT(vertex), mid + 1, right);
    }
    return val;
  }

  int query(int x, int l) {
    return query(x, l, 0, 0, size - 1);
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
      scanf("%d %d", &arg1, &arg2);
      printf("%d\n", st.query(arg1, arg2));
    }
  }

  return 0;
}

