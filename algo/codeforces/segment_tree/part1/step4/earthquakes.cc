#include <cstdio>
#include <cstdint>
#include <cmath>
#include <vector>
#include <limits>

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<std::vector<int *>> points;
  std::vector<int> array;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n) / std::log(2)));
    array.assign(size, 0);
    build_tree(0, 0, size - 1);
  }

  void build_tree(int vertex, int left, int right) {
    if (left == right) {
      points[vertex].assign(1, &array[vertex]);
      return;
    }

    int mid = (left + right) / 2;
    build_tree(LEFT(vertex), left, mid);
    build_tree(RIGHT(vertex), mid + 1, right);

    points[vertex].assign(right - left + 1, nullptr);

/*
    int size = points[LEFT(vertex)].size();
    for (int i = 0; i < size; i++) {
      points[vertex][i] = points[LEFT(vertex)][i];
    }
    for (int i = 0; i < size; i++) {
      points[vertex][size + i] = points[RIGHT(vertex)][i];
    }
 */
  }

  void merge(int vertex, int left, int right) {
    int size = points[vertex].size();
    int p = 0, q = 0;

    for (int i = 0; i < size; i++) {
      if (q == size / 2 || *points[left][p] < *points[right][q]) {
        points[vertex][i] = points[left][p];
        p++;
      } else {
        points[vertex][i] = points[right][q];
        q++;
      }
    }
  }

  void update(int index, int value, int vertex, int left, int right) {
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

    //merge(vertex, LEFT(vertex), RIGHT(vertex));
  }

  void update(int index, int value) {
    update(index, value, 0, 0, size - 1);
  }

/*
  int query(int a, int b, int p, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right && array[vertex] > p) {
      return 0;
    }

    if (a <= left && b >= right && left == right) {
      if (array[vertex] == 0) {
        return 0;
      }
      array[vertex] = 0;
      return 1;
    }

    int mid = (left + right) / 2;
    int l = query(a, b, p, LEFT(vertex), left, mid);
    int r = query(a, b, p, RIGHT(vertex), mid + 1, right);

    array[vertex] = std::min(array[LEFT(vertex)], array[RIGHT(vertex)]);
    return l + r;
  }

  int query(int a, int b, int p) {
    return query(a, b, p, 0, 0, size - 1);
  }

*/
};

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int op, arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d", &arg1, &arg2);
      st.update(arg1, arg2);
    } else {
      scanf("%d %d %d", &arg1, &arg2, &arg3);
    }
  }

  return 0;
}


