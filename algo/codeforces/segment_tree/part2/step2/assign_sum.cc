/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. update(a, b, v) - ustawia elementy z przedziału a do b na wartość v.
    2. query(a, b)     - zwraca sumę z przedziału.
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
  std::vector<int64_t> assign;
  std::vector<int64_t> sum;

  const int64_t NO_SET = std::numeric_limits<int64_t>::min();

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    assign.assign(size * 2, NO_SET);
    sum.assign(size * 2, 0);
  }

  void lazy_propagation(int vertex, int n) {
    if (assign[vertex] != NO_SET) {
      assign[LEFT(vertex)] = assign[vertex];
      assign[RIGHT(vertex)] = assign[vertex];
      sum[LEFT(vertex)] = (n / 2) * assign[vertex];
      sum[RIGHT(vertex)] = (n / 2) * assign[vertex];
      assign[vertex] = NO_SET;
    }
  }

  void update(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      assign[vertex] = value;
      sum[vertex] = (right - left + 1) * value;
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    sum[vertex] = sum[LEFT(vertex)] + sum[RIGHT(vertex)];
  }

  void update(int a, int b, int64_t value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int64_t query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right) {
      return sum[vertex];
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    int64_t l = query(a, b, LEFT(vertex), left, mid);
    int64_t r = query(a, b, RIGHT(vertex), mid + 1, right);
    return l + r;
  }

  int64_t query(int a, int b) {
    return query(a, b, 0, 0, size - 1);
  }
};

/*
int main(void)
{
  #define SIZE 8
  int arr[SIZE] = {2, 7, 1, 3, 5, 1, 2, 8};
  SegmentTree st(SIZE);

  for (int i = 0; i < SIZE; i++) {
    st.update(i, i, arr[i]);
  }

  st.update(0, SIZE - 1, 1);
  printf("%d\n", st.query(0, 1));

  return 0;
}
*/

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
      printf("%lld\n", st.query(arg1, arg2 - 1));
    }
  }
  return 0;
}


