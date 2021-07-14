/*
  Drzewo przedziałowe.

  - max(a, b)    - spójny podciąg elementów od a do b o największej sumie.
  - set(a, b, v) - ustaw wszystkie elementy z przedziału a do b na wartość v.
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct Node {
  int64_t seg;
  int64_t pref;
  int64_t suff;
  int64_t sum;
};

struct SegmentTree {

  const int64_t NO_SET = std::numeric_limits<int64_t>::max();
  const Node NEUTRAL = { 0, 0, 0, 0 };

  int size;
  std::vector<Node> max;
  std::vector<int64_t> assign;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    max.assign(size * 2, NEUTRAL);
    assign.assign(size * 2, NO_SET);
  }

  Node single(int64_t value, int64_t n) {
    value *= n;
    if (value > 0) {
      return { value, value, value, value};
    }
    return { 0, 0, 0, value };
  }

  Node merge(Node a, Node b) {
    Node c;
    c.seg = std::max(a.seg, std::max(b.seg, a.suff + b.pref));
    c.pref = std::max(a.pref, a.sum + b.pref);
    c.suff = std::max(b.suff, a.suff + b.sum);
    c.sum = a.sum + b.sum;
    return c;
  }

  void lazy_propagation(int vertex, int n) {
    if (assign[vertex] != NO_SET) {
      assign[LEFT(vertex)] = assign[vertex];
      assign[RIGHT(vertex)] = assign[vertex];
      max[LEFT(vertex)] = single(assign[vertex], n / 2);
      max[RIGHT(vertex)] = single(assign[vertex], n / 2);
      assign[vertex] = NO_SET;
    }
  }

  void update(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      assign[vertex] = value;
      max[vertex] = single(value, right - left + 1);
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    max[vertex] = merge(max[LEFT(vertex)], max[RIGHT(vertex)]);
  }

  void update(int a, int b, int value) {
    update(a, b, value, 0, 0, size - 1);
  }

  Node query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return NEUTRAL;
    }

    if (a <= left && b >= right) {
      return max[vertex];
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (right + left) / 2;
    Node l = query(a, b, LEFT(vertex), left, mid);
    Node r = query(a, b, RIGHT(vertex), mid + 1, right);

    return merge(l, r);
  }

  int64_t query(int a, int b) {
    return query(a, b, 0, 0, size - 1).seg;
  }
};

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &arg1, &arg2, &arg3);
    st.update(arg1, arg2 - 1, arg3);
    printf("%lld\n", st.query(0, n - 1));
  }

  return 0;
}

