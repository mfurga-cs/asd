/*
  Drzewo przedziałwe do zliczania inwersji permutacji n elementowej.
  Tworzymy drzewo typu suma przedziału rozmiaru n. Idziemy od lewe do prawej
  i ustawiamy wartość 1 na polu o indeksie A[i].
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

  SegmentTree(int64_t *arr, int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    array.resize(size * 2);
    for (int i = 0; i < n; i++) {
      array[size - 1 + i] = arr[i];
    }
    build_tree(0, 0, size - 1);
  }

  void build_tree(int vertex, int left, int right) {
    if (left == right) {
      return;
    }
    int mid = (left + right) / 2;
    build_tree(LEFT(vertex), left, mid);
    build_tree(RIGHT(vertex), mid + 1, right);
    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
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

    array[vertex] = array[LEFT(vertex)] + array[RIGHT(vertex)];
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
    return sum(a, b, 0, 0, size - 1);
  }

};

int main(void)
{
  int n;
  scanf("%d", &n);

  SegmentTree segtree(n + 1);

  int v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &v);
    printf("%d ", segtree.sum(v + 1, n));
    segtree.set(v, 1);
  }

  printf("\n");

  return 0;
}

