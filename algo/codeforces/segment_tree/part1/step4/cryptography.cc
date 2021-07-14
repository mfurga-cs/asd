/*
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

typedef struct {
  int x00, x01, x10, x11;
} matrix_t;

matrix_t matrix_mul(int r, matrix_t a, matrix_t b)
{
  matrix_t c;
  c.x00 = ((a.x00 * b.x00) % r + (a.x01 * b.x10) % r) % r;
  c.x01 = ((a.x00 * b.x01) % r + (a.x01 * b.x11) % r) % r;
  c.x10 = ((a.x10 * b.x00) % r + (a.x11 * b.x10) % r) % r;
  c.x11 = ((a.x10 * b.x01) % r + (a.x11 * b.x11) % r) % r;
  return c;
}

void matrix_print(matrix_t a)
{
  printf("%d %d\n%d %d\n\n", a.x00, a.x01, a.x10, a.x11);
}

struct SegmentTree {
  int size;
  std::vector<matrix_t> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.resize(2 * size);
  }

  void set(int r, int index, matrix_t value, int vertex, int left, int right) {
    if (left == right) {
      array[vertex] = value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(r, index, value, LEFT(vertex), left, mid);
    } else {
      set(r, index, value, RIGHT(vertex), mid + 1, right);
    }

    array[vertex] = matrix_mul(r, array[LEFT(vertex)], array[RIGHT(vertex)]);
  }

  void set(int r, int index, matrix_t value) {
    set(r, index, value, 0, 0, size - 1);
  }

  matrix_t mul(int r, int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return {1, 0, 0, 1};
    }

    if (a <= left && b >= right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    matrix_t ll = mul(r, a, b, LEFT(vertex), left, mid);
    matrix_t rr = mul(r, a, b, RIGHT(vertex), mid + 1, right);

    return matrix_mul(r, ll, rr);
  }

  matrix_t mul(int r, int a, int b) {
    return mul(r, a, b, 0, 0, size - 1);
  }

};

int main(void)
{
  int r, n, m;
  scanf("%d %d %d", &r, &n , &m);
  SegmentTree st(n);

  matrix_t a;
  for (int i = 0; i < n; i++) {
    scanf("%d %d %d %d", &a.x00, &a.x01, &a.x10, &a.x11);
    st.set(r, i, a);
  }

  int arg1, arg2;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &arg1, &arg2);
    matrix_print(st.mul(r, arg1 - 1, arg2 - 1));
  }

  return 0;
}

