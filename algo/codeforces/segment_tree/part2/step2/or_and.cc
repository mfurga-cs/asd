/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. update(a, b, v) - operacja or z wartością v na elementach z przedziału a do b.
    2. query(a, b)     - operacja and na przedziale a do b.
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
  std::vector<int64_t> band;
  std::vector<int64_t> bor;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    band.assign(size * 2, 0);
    bor.assign(size * 2, 0);
  }

  void update(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      band[vertex] |= value;
      bor[vertex] |= value;
      return;
    }

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    band[vertex] = (band[LEFT(vertex)] & band[RIGHT(vertex)]) | bor[vertex];
  }

  void update(int a, int b, int64_t value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int64_t query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0xffffffffffffffffLL;
    }

    if (a <= left && b >= right) {
      return band[vertex];
    }

    int mid = (left + right) / 2;
    int64_t l = query(a, b, LEFT(vertex), left, mid);
    int64_t r = query(a, b, RIGHT(vertex), mid + 1, right);
    return (l & r) | bor[vertex];
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


