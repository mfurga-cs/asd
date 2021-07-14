#include <cstdio>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

class SegmentTree {
  private:
  int _size;
  std::vector<std::pair<int, int>> _array;

  void set(int index, int value, int vertex, int left, int right) {
    if (left == right) {
      _array[vertex] = std::make_pair(value, 1);
      return;
    }

    int mid = (left + right) / 2;
    if (index <= mid) {
      set(index, value, LEFT(vertex), left, mid);
    } else {
      set(index, value, RIGHT(vertex), mid + 1, right);
    }

    std::pair<int, int> l = _array[LEFT(vertex)];
    std::pair<int, int> r = _array[RIGHT(vertex)];

    if (l.first < r.first) {
      _array[vertex] = l;
    } else if (l.first > r.first) {
      _array[vertex] = r;
    } else {
      _array[vertex] = std::make_pair(l.first, l.second + r.second);
    }
  }

  std::pair<int, int> min(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return std::make_pair(std::numeric_limits<int>::max(), 0);
    }

    if (a <= left && b >= right) {
      return _array[vertex];
    }

    int mid = (left + right) / 2;
    std::pair<int, int> l = min(a, b, LEFT(vertex), left, mid);
    std::pair<int, int> r = min(a, b, RIGHT(vertex), mid + 1, right);

    if (l.first < r.first) {
      return l;
    }

    if (l.first > r.first) {
      return r;
    }

    return std::make_pair(l.first, l.second + r.second);
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
    _array.assign(_size * 2, std::make_pair<int, int>(std::numeric_limits<int>::max(), 1));
  }

  void set(int index, int value) {
    set(index, value, 0, 0, _size - 1);
  }

  std::pair<int, int> min(int a, int b) {
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
      std::pair<int, int> res = segtree.min(arg1, arg2 - 1);
      printf("%d %d\n", res.first, res.second);
    }
  }

  return 0;
}

