#include <cstdio>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

class SegmentTree {
  private:
  int _size;
  std::vector<int> _array;

  void set(int index, int value, int vertex, int left, int right) {
    if (left == right) {
      _array[vertex] = value;
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(index, value, LEFT(vertex), left, mid);
    } else {
      set(index, value, RIGHT(vertex), mid + 1, right);
    }

    _array[vertex] = std::min(_array[LEFT(vertex)], _array[RIGHT(vertex)]);
  }

  int min(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return std::numeric_limits<int>::max();
    }

    if (a <= left && b >= right) {
      return _array[vertex];
    }

    int mid = (left + right) / 2;
    int l = min(a, b, LEFT(vertex), left, mid);
    int r = min(a, b, RIGHT(vertex), mid + 1, right);
    return std::min(l, r);
  }

  static int next_pow_2(int n) {
    int i = 1;
    while (i < n) {
      i *= 2;
    }
    return i;
  }

  public:
  SegmentTree(int n) {
    _size = next_pow_2(n);
    _array.assign(_size * 2, std::numeric_limits<int>::max());
  }

  void set(int index, int value) {
    set(index, value, 0, 0, _size - 1);
  }

  int min(int a, int b) {
    return min(a, b, 0, 0, _size - 1);
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

  int op, arg1, arg2;
  for (int i = 0; i < m; i++) {
    scanf("%d %d %d", &op, &arg1, &arg2);

    if (op == 1) {
      segtree.set(arg1, arg2);
    } else {
      printf("%d\n", segtree.min(arg1, arg2 - 1));
    }
  }

  return 0;
}

