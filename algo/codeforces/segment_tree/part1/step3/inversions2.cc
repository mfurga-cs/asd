/*
  Drzewo przedziałowe na tablicy (elementy 0 lub 1).

  Operacje:
    1. find(k) - zwraca indeks k-tej (numeracja od 0) jedynki z prawej
                 strony w ciągu lub -1 jeśli nie ma.
    2. set(i)  - ustawia wartość na podanym indeksie i na przeciwną.
*/

#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <stack>

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

    if (array[RIGHT(vertex)] >= k) {
      return find(k, RIGHT(vertex), mid + 1, right);
    } else{
      return find(k - array[RIGHT(vertex)], LEFT(vertex), left, mid);
    }
  }

  int find(int k) {
    return find(k, 0, 0, size - 1);
  }
};

int main(void)
{
  int n;
  scanf("%d", &n);
  SegmentTree st(n);

  for (int i = 0; i < n; i++) {
    st.set(i);
  }

  std::stack<int> s1;
  std::stack<int> s2;

  int k, v;
  for (int i = 0; i < n; i++) {
    scanf("%d", &k);
    s1.push(k);
  }

  while (!s1.empty()) {
    k = s1.top();
    s1.pop();

    v = st.find(k + 1);;
    st.set(v);
    s2.push(v + 1);
  }

  while (!s2.empty()) {
    v = s2.top();
    s2.pop();
    printf("%d ", v);
  }
  printf("\n");

  return 0;
}

