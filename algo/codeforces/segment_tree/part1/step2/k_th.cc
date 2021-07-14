/*
  Drzewo przedziałowe na tablicy (elementy 0 lub 1).
  Operacje:
    1. find(k) - zwraca indeks k-tej jedynki w ciągu lub -1 jeśli nie ma.
    2. set(i)  - ustawia wartość na podanym indeksie i na przeciwną.
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<int64_t> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.assign(size * 2, 0);
  }

  SegmentTree(int64_t *arr, int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.resize(size * 2);

    printf("size: %d\n", size);

    for (int i = 0; i < n; i++) {
      array[size - 1 + i] = arr[i];
    }

    _build_tree(0, 0, size - 1);
  }

  void _build_tree(int vertex, int left, int right) {
    if (left == right) {
      return;
    }

    int mid = (left + right) / 2;

    _build_tree(LEFT(vertex), left, mid);
    _build_tree(RIGHT(vertex), mid + 1, right);

    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
  }

  void set(int index, int vertex, int left, int right) {
    if (left == right) {
     array[vertex] = 1 - array[vertex];
      return;
    }

    int mid = (left + right) / 2;

    if (index <= mid) {
      set(index, LEFT(vertex), left, mid);
    } else {
      set(index, RIGHT(vertex), mid + 1, right);
    }

    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
  }

  void set(int index) {
    set(index, 0, 0, size - 1);
  }

  int find(int k, int vertex, int left, int right) {
    if (left == right) {
      return array[vertex] == 1 && k == 1 ? left : -1;
    }

    int mid = (left + right) / 2;

    if (array[LEFT(vertex)] >= k) {
      return find(k, LEFT(vertex), left, mid);
    } else{
      return find(k - array[LEFT(vertex)], RIGHT(vertex), mid + 1, right);
    }
  }

  int find(int k) {
    return find(k, 0, 0, size - 1);
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
    if (v == 1) {
      segtree.set(i);
    }
  }

  int op, arg;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &op, &arg);
    if (op == 1) {
      segtree.set(arg);
    } else {
      printf("%d\n", segtree.find(arg + 1));
    }
  }

  return 0;
}

