/*
  Drzewo przedziałowe na tablicy (elementy 0 lub 1).
  Operacje:
    1. find(x, l) - zwraca minimalny indeks i takie że i >= l i A[i] >= x.
    2. set(i, v)  - ustawia wartość na podanym indeksie i na v.
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int _size;
  std::vector<int64_t> _array;

  SegmentTree(int n) {
    _size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    _array.assign(_size * 2, 0);
  }

  SegmentTree(int64_t *arr, int n) {
    _size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    _array.resize(_size * 2);

    for (int i = 0; i < n; i++) {
      _array[_size - 1 + i] = arr[i];
    }

    _build_tree(0, 0, _size - 1);
  }

  void _build_tree(int vertex, int left, int right) {
    if (left == right) {
      return;
    }

    int mid = (left + right) / 2;

    _build_tree(LEFT(vertex), left, mid);
    _build_tree(RIGHT(vertex), mid + 1, right);

    _array[vertex] = std::max(_array[LEFT(vertex)], _array[RIGHT(vertex)]);
  }

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

    _array[vertex] = std::max(_array[LEFT(vertex)], _array[RIGHT(vertex)]);
  }

  void set(int index, int value) {
    set(index, value, 0, 0, _size - 1);
  }

  int find(int x, int l, int vertex, int left, int right) {

    if (_array[vertex] < x || right < l) {
      return -1;
    }

    if (left == right) {
      return left;
    }

    int mid = (left + right) / 2;

    int v = find(x, l, LEFT(vertex), left, mid);
    if (v != -1) {
      return v;
    }
    return find(x, l, RIGHT(vertex), mid + 1, right);
  }

  int find(int x, int l) {
    return find(x, l, 0, 0, _size - 1);
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
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d", &arg1, &arg2);
      segtree.set(arg1, arg2);
    } else {
      scanf("%d %d", &arg1, &arg2);
      printf("%d\n", segtree.find(arg1, arg2));
    }
  }

  return 0;
}

