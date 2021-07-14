/*
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

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.assign(size * 2, 0);
  }

  void set(int index, int value, int vertex, int left, int right) {
    if (left == right) {
      array[vertex] = value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(index, value, LEFT(vertex), left, mid);
    } else {
      set(index, value, RIGHT(vertex), mid + 1, right);
    }

    if (right - left == 1) {
      array[vertex] = array[LEFT(vertex)] - array[RIGHT(vertex)];
    } else {
      array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
    }
  }

  void set(int index, int value) {
    set(index, value, 0, 0, size - 1);
  }

  int sum(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    int l = sum(a, b, LEFT(vertex), left, mid);
    int r = sum(a, b, RIGHT(vertex), mid + 1, right);

    return l + r;
  }

  int sum(int a, int b) {
    if (a % 2 == 0) {
      return sum(a, b, 0, 0, size - 1);
    }
    return sum(a, a, 0, 0, size - 1) - sum(a + 1, b, 0, 0, size - 1);
  }

};

int main(void)
{
  int n, m;
  scanf("%d", &n);
  SegmentTree st(n);

  int v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v);
    st.set(i, v);
  }

  scanf("%d", &m);

  int op, arg1, arg2;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &op, &arg1, &arg2);
    if (op == 0) {
      st.set(arg1 - 1, arg2);
    } else {
      printf("%d\n", st.sum(arg1 - 1, arg2 - 1));
    }
  }

  return 0;
}

