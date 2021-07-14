#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

typedef struct {
  int64_t cnt[41];
} node_t;

struct SegmentTree {
  int size;
  std::vector<node_t> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.resize(2 * size);
  }

  node_t merge(node_t a, node_t b) {
    node_t c = { {0LL} };
    for (int i = 0; i <= 40; i++) {
      c.cnt[i] = a.cnt[i] || b.cnt[i];
    }
    return c;
  }

  void update(int index, node_t value, int vertex, int left, int right) {
    if (left == right) {
      array[vertex] = value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      update(index, value, LEFT(vertex), left, mid);
    } else {
      update(index, value, RIGHT(vertex), mid + 1, right);
    }

    array[vertex] = merge(array[LEFT(vertex)], array[RIGHT(vertex)]);
  }

  void update(int index, int value) {
    node_t node = { {0LL} };
    node.cnt[value] = 1LL;
    update(index, node, 0, 0, size - 1);
  }

  node_t query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return { {0LL} };
    }

    if (a <= left && b >= right) {
      return array[vertex];
    }

    int mid = (left + right) / 2;
    node_t l = query(a, b, LEFT(vertex), left, mid);
    node_t r = query(a, b, RIGHT(vertex), mid + 1, right);

    return merge(l, r);
  }

  int64_t query(int a, int b) {
    node_t node = query(a, b, 0, 0, size - 1);
    int c = 0;
    for (int i = 0; i <= 40; i++) {
      c += node.cnt[i];
    }
    return c;
  }

};

int main(void)
{
  int n, q;
  scanf("%d %d", &n, &q);

  SegmentTree st(n);

  int v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v);
    st.update(i, v);
  }

  int op, arg1, arg2;
  for (int i = 0; i < q; i++) {
    scanf("%d %d %d", &op, &arg1, &arg2);
    if (op == 1) {
      printf("%lld\n", st.query(arg1 - 1, arg2 - 1));
    } else {
      st.update(arg1 - 1, arg2);
    }
  }

  return 0;
}

