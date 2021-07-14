/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. update(a, b, s, d) - do każdego elementu na przedziale a do b dodać (a <= i <= b) xi = s + d * (i - l).
    2. query(i)           - zwraca wartość elementu i-tego.
*/

#include <cstdio>
#include <cmath>
#include <vector>
#include <limits>
#include <cassert>

typedef long long int int64;

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<int64> param_s;
  std::vector<int64> param_d;
  std::vector<bool> op;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    param_s.assign(size * 2, 0);
    param_d.assign(size * 2, 0);
    op.assign(size * 2, false);
  }

  void lazy_propagation(int vertex, int left, int right) {
    int mid = (left + right) / 2;
    if (op[vertex]) {
      param_s[LEFT(vertex)] += param_s[vertex];
      param_d[LEFT(vertex)] += param_d[vertex];
      param_s[RIGHT(vertex)] += param_s[vertex] + ((mid - left + 1) * param_d[vertex]);
      param_d[RIGHT(vertex)] += param_d[vertex];

      param_s[vertex] = 0;
      param_d[vertex] = 0;
      op[LEFT(vertex)] = true;
      op[RIGHT(vertex)] = true;
      op[vertex] = false;
    }
  }

  void update(int a, int b, int64 s, int64 d, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
//      printf("SAVING: left=%d right=%d s=%d d=%d\n", left, right, s, d);
      param_s[vertex] += s;
      param_d[vertex] += d;
      op[vertex] = true;
      return;
    }

    lazy_propagation(vertex, left, right);

    int mid = (left + right) / 2;

    int64 v = std::min(mid, b) - std::max(left, a) + 1;
//    printf("left: %d; right: %d v: %d\n", left, right, v);

    update(a, b, s, d, LEFT(vertex), left, mid);
    update(a, b, s + std::max(v, 0LL) * d, d, RIGHT(vertex), mid + 1, right);
  }

  void update(int a, int b, int64 s, int64 d) {
    update(a, b, s, d, 0, 0, size - 1);
  }

  int64 query(int i, int vertex, int left, int right) {
    if (left == right) {
      return param_s[vertex];
    }

    lazy_propagation(vertex, left, right);

    int mid = (left + right) / 2;
    if (i <= mid) {
      return query(i, LEFT(vertex), left, mid);
    }
    return query(i, RIGHT(vertex), mid + 1, right);
  }

  int64 query(int i) {
    return query(i, 0, 0, size - 1);
  }
};

#define SIZE 8

void TEST(SegmentTree &st, int *res) {
  for (int i = 0; i < SIZE; i++) {
    printf("%d %d\n", st.query(i), res[i]);
    assert(st.query(i) == res[i]);
  }
}

/*
int main(void)
{
  int arr[SIZE] = {0, 0, 0, 0, 0, 0, 0, 0};
  SegmentTree st(SIZE);

  for (int i = 0; i < SIZE; i++) {
    st.update(i, i, arr[i], 10);
  }

  TEST(st, arr);
  st.update(0, SIZE - 1, 1, 1);
  int res1[] = {1, 2, 3, 4, 5, 6, 7, 8};
  TEST(st, res1);

  st.update(3, 4, 1, 2);
  int res2[] = {1, 2, 3, 5, 8, 6, 7, 8};
  TEST(st, res2);

  st.update(4, 7, 1, 1);
  st.update(4, 7, 1, 1);
  st.update(5, 6, 2, 3);
  int res3[] = {1, 2, 3, 5, 10, 12, 18, 16};
  TEST(st, res3);

  st.update(0, 4, 1, 1);
  int res4[] = {2, 4, 6, 9, 15, 12, 18, 16};
  TEST(st, res4);

  st.update(0, SIZE - 1, 1, 1);
  int res5[] = {3, 6, 9, 13, 20, 18, 25, 24};
  TEST(st, res5);

  st.update(5, SIZE - 1, 7, 1);
  int res6[] = {3, 6, 9, 13, 20, 25, 33, 33};
  TEST(st, res6);

  st.update(2, 6, 2, 3);
  int res7[] = {3, 6, 11, 18, 28, 36, 47, 33};
  TEST(st, res7);

  return 0;
}

*/
int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int op, arg1, arg2, arg3, arg4;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d %d %d", &arg1, &arg2, &arg3, &arg4);
      st.update(arg1 - 1, arg2 - 1, arg3, arg4);
    } else {
      scanf("%d", &arg1);
      printf("%lld\n", st.query(arg1 - 1));
    }
  }
  return 0;
}

