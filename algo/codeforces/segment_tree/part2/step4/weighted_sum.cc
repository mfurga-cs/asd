/*
  Drzewo przedziałowe na tablicy.
*/

#include <bits/stdc++.h>

typedef long long int64;

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<int64> param_a;
  std::vector<int64> param_b;
  std::vector<int64> upd;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    param_a.resize(2 * size, 0LL);
    param_b.resize(2 * size, 0LL);
    upd.resize(2 * size, 0LL);
  }

  void single(int vertex, int length, int64 value) {
    if (length == 1) {
      param_b[vertex] = 0;
    } else {
      param_b[vertex] = param_b[vertex] + (int64)(((int64)length / 2) * (1 + (int64)length)) * value - (int64)length * value;
    }
    param_a[vertex] += length * value;
    upd[vertex] += value;
  }

  void merge(int vertex, int length) {
    param_a[vertex] = param_a[LEFT(vertex)] + param_a[RIGHT(vertex)];
    param_b[vertex] = param_b[LEFT(vertex)] + param_b[RIGHT(vertex)] + param_a[RIGHT(vertex)] * length / 2;
  }

  void lazy_propagation(int vertex, int length) {
    if (upd[vertex] != 0LL) {
      single(LEFT(vertex), length / 2, upd[vertex]);
      single(RIGHT(vertex), length / 2, upd[vertex]);
      upd[vertex] = 0LL;
    }
  }

  void update(int a, int b, int64 value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      single(vertex, right - left + 1, value);
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    merge(vertex, right - left + 1);
  }

  void update(int a, int b, int64 value) {
    update(a, b, value, 0, 0, size - 1);
  }

  int64 query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0LL;
    }

    if (a <= left && b >= right) {
      int64 x = left - a + 1;
      if (left == right) {
        assert(param_b[vertex] == 0);
      }
      return param_a[vertex] * x + param_b[vertex];
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    int64 l = query(a, b, LEFT(vertex), left, mid);
    int64 r = query(a, b, RIGHT(vertex), mid + 1, right);
    return l + r;
  }

  int64 query(int a, int b) {
    return query(a, b, 0, 0, size - 1);
  }
};

/*
int main(void)
{
  #define SIZE 8

  SegmentTree st(SIZE);
  int64 arr[SIZE] = {1,2,3,4,5,6,7,8};

  for (int i = 0; i < SIZE; i++) {
    st.update(i, i, arr[i]);
  }


  assert(st.query(0, SIZE - 1) == 204);
  assert(st.query(0, 3) == 30);
  assert(st.query(0, 4) == 55);
  assert(st.query(0, 5) == 91);

  assert(st.query(1, 2) == 8);
  assert(st.query(1, 3) == 20);
  assert(st.query(1, 4) == 40);
  assert(st.query(1, 5) == 70);
  assert(st.query(1, 6) == 112);

  assert(st.query(3, 6) == 60);

  st.update(3, 6, 3);
  assert(st.query(3, 6) == 90);
  st.update(3, 6, 1);
  assert(st.query(3, 6) == 100);
  st.update(3, 6, 2);
  assert(st.query(3, 6) == 120);
  st.update(3, 6, -6);
  assert(st.query(3, 6) == 60);

  for (int i= 0; i < SIZE; i++) {
    printf("%lld ", st.query(i, i));
  }
  printf("\n");

  st.update(0, SIZE - 1, 1);
  assert(st.query(3, 6) == 70);
  st.update(0, SIZE - 1, -1);

  st.update(7, 7, 3);
  assert(st.query(0, SIZE - 1) == 228);
  st.update(7, 7, -3);
  assert(st.query(0, SIZE - 1) == 204);

  st.update(3, 6, 3);
  st.update(6, 6, 1);
  st.update(4, 5, 2);
  assert(st.query(0, SIZE - 1) == 299);
  assert(st.query(2, 3) == 17);

  for (int i= 0; i < SIZE; i++) {
    printf("%lld ", st.query(i, i));
  }
  printf("\n");

  assert(st.query(2, 4) == 47);

  return 0;
}

*/

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  SegmentTree st(n);

  int64 v;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &v);
    st.update(i, i, v);
  }

  int64 op, arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%lld", &op);
    if (op == 1) {
      scanf("%lld %lld %lld", &arg1, &arg2, &arg3);
      st.update(arg1 - 1, arg2 - 1, arg3);
    } else {
      scanf("%lld %lld", &arg1, &arg2);
      printf("%lld\n", st.query(arg1 - 1, arg2 - 1));
    }
  }

  return 0;
}


