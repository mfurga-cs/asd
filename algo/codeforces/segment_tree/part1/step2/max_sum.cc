/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. max(a, b) - zwraca najdłuższy spójny podciąg z największą sumą elemnetów w przedziale
                   od a do b. O(logn)
    2. set(i, v) - ustawia element o indeksie i na podaną wartość. O(logn)
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmnetTreeNode {
  int64_t seg;
  int64_t pref;
  int64_t suff;
  int64_t sum;
};

struct SegmentTree {
  int _size;
  std::vector<SegmnetTreeNode> _array;

  const SegmnetTreeNode NEUTRAL = {0LL, 0LL, 0LL, 0LL};

  SegmentTree(int n) {
    _size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    _array.assign(_size * 2, NEUTRAL);
  }

  SegmnetTreeNode _single(int value) {
    if (value > 0) {
      return {value, value, value, value};
    }
    return {0, 0, 0, value};
  }

  SegmnetTreeNode _merge(SegmnetTreeNode a, SegmnetTreeNode b) {
    SegmnetTreeNode c;
    c.seg = std::max(a.seg, std::max(b.seg, a.suff + b.pref));
    c.pref = std::max(a.pref, a.sum + b.pref);
    c.suff = std::max(b.suff, b.sum + a.suff);
    c.sum = a.sum + b.sum;
    return c;
  }

  void set(int index, int value, int vertex, int left, int right) {
    if (left == right) {
     _array[vertex] = _single(value);
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(index, value, LEFT(vertex), left, mid);
    } else {
      set(index, value, RIGHT(vertex), mid + 1, right);
    }

    _array[vertex] = _merge(_array[LEFT(vertex)], _array[RIGHT(vertex)]);
  }

  void set(int index, int value) {
    set(index, value, 0, 0, _size - 1);
  }

  SegmnetTreeNode max(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return NEUTRAL;
    }

    if (a <= left && b >= right) {
      return _array[vertex];
    }

    int mid = (left + right) / 2;
    SegmnetTreeNode l = max(a, b, LEFT(vertex), left, mid);
    SegmnetTreeNode r = max(a, b, RIGHT(vertex), mid + 1, right);

    return _merge(l, r);
  }

  int64_t max(int a, int b) {
    return max(a, b, 0, 0, _size - 1).seg;
  }
};


int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);

  SegmentTree segtree(n);
  int v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v);
    segtree.set(i, v);
  }

  printf("%lld\n", segtree.max(0, n - 1));

  int index, value;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &index, &value);
    segtree.set(index, value);
    printf("%lld\n", segtree.max(0, n - 1));
  }
  return 0;
}

