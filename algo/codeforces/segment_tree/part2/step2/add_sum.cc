/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. update(a, b, v) - dodaje do elementów z przedziału a do b wartość v.
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
  std::vector<int64_t> add;
  std::vector<int64_t> sum;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    sum.assign(size * 2, 0);
    add.assign(size * 2, 0);
  }

  int64_t update_opt(int64_t a, int64_t b, int64_t n) {
    return a + b * n;
  }

  int64_t query_opt(int64_t a, int64_t b) {
    return a + b;
  }

  void update(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      sum[vertex] = update_opt(sum[vertex], value, right - left + 1);
      add[vertex] = update_opt(add[vertex], value, 1);
      return;
    }

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    sum[vertex] = update_opt(query_opt(sum[LEFT(vertex)], sum[RIGHT(vertex)]), add[vertex], right - left + 1);
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

    int mid = (left + right) / 2;
    int64_t l = query(a, b, LEFT(vertex), left, mid);
    int64_t r = query(a, b, RIGHT(vertex), mid + 1, right);
    return update_opt(query_opt(l, r), add[vertex], std::min(b, right) - std::max(a, left) + 1);
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


