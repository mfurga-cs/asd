/*
  Drzewo przedziałowe.

  - update(a, b) - zmienia elementy z przedziału od a do b na przeciwne.
  - query(k)     - zwraca indeks pierwszego wystąpienia 1 w ciągu.
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
  std::vector<int64_t> sum;
  std::vector<int64_t> assign;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    sum.assign(size * 2, 0);
    assign.assign(size * 2, 0);
  }

  void lazy_propagation(int vertex, int n) {
    if (assign[vertex]) {
      assign[LEFT(vertex)] = 1 - assign[LEFT(vertex)];
      assign[RIGHT(vertex)] = 1 - assign[RIGHT(vertex)];
      sum[LEFT(vertex)] = (n / 2) - sum[LEFT(vertex)];
      sum[RIGHT(vertex)] = (n / 2) - sum[RIGHT(vertex)];
      assign[vertex] = 0;
    }
  }

  void update(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      assign[vertex] = 1 - assign[vertex];
      sum[vertex] = (right - left + 1) - sum[vertex];
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    update(a, b, LEFT(vertex), left, mid);
    update(a, b, RIGHT(vertex), mid + 1, right);

    sum[vertex] = sum[LEFT(vertex)] + sum[RIGHT(vertex)];
  }

  void update(int a, int b) {
    update(a, b, 0, 0, size - 1);
  }

  int query(int k, int vertex, int left, int right) {
    if (left == right) {
      return sum[vertex] == 1 && k == 1 ? left : -1;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    if (sum[LEFT(vertex)] >= k) {
      return query(k, LEFT(vertex), left, mid);
    }
    return query(k - sum[LEFT(vertex)], RIGHT(vertex), mid + 1, right);
  }

  int query(int k) {
    return query(k, 0, 0, size - 1);
  }
};

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int op, arg1, arg2;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d", &arg1, &arg2);
      st.update(arg1, arg2 - 1);
    } else {
      scanf("%d", &arg1);
      printf("%d\n", st.query(arg1 + 1));
    }
  }

  return 0;
}

