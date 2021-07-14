/*
  Drzewo przedziałowe na tablicy.
  Operacje:
    1. assign(a, b, v) - ustawia elementy z przedziału od a do b na wartość v.
    2. add(a, b, v)    - dodaje do elementów z przedziału od a do b wartość v.
    3. query(a, b)     - zwraca sumę z przedziału.
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
  std::vector<int64_t> sum;
  std::vector<int64_t> add_op;
  std::vector<int64_t> ass_op;

  const int64_t NO_OPT = std::numeric_limits<int64_t>::min();

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    sum.assign(size * 2, 0);
    add_op.assign(size * 2, NO_OPT);
    ass_op.assign(size * 2, NO_OPT);
  }

  void lazy_propagation(int vertex, int n) {
    if (add_op[vertex] == NO_OPT && ass_op[vertex] == NO_OPT) {
      return;
    }

    if (ass_op[vertex] != NO_OPT) {
      sum[LEFT(vertex)] = (n / 2) * ass_op[vertex];
      sum[RIGHT(vertex)] = (n / 2) * ass_op[vertex];

      ass_op[LEFT(vertex)] = ass_op[vertex];
      ass_op[RIGHT(vertex)] = ass_op[vertex];
      add_op[LEFT(vertex)] = NO_OPT;
      add_op[RIGHT(vertex)] = NO_OPT;
      ass_op[vertex] = NO_OPT;
    }

    if (add_op[vertex] != NO_OPT) {
      sum[LEFT(vertex)] += (n / 2) * add_op[vertex];
      sum[RIGHT(vertex)] += (n / 2) * add_op[vertex];

      add_op[LEFT(vertex)] = (add_op[LEFT(vertex)] == NO_OPT) ? add_op[vertex] : add_op[LEFT(vertex)] + add_op[vertex];
      add_op[RIGHT(vertex)] = (add_op[RIGHT(vertex)] == NO_OPT) ? add_op[vertex] : add_op[RIGHT(vertex)] + add_op[vertex];
      add_op[vertex] = NO_OPT;
    }
  }

  void assign(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      sum[vertex] = (right - left + 1) * value;
      add_op[vertex] = NO_OPT;
      ass_op[vertex] = value;
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    assign(a, b, value, LEFT(vertex), left, mid);
    assign(a, b, value, RIGHT(vertex), mid + 1, right);

    sum[vertex] = sum[LEFT(vertex)] + sum[RIGHT(vertex)];
  }

  void assign(int a, int b, int64_t value) {
    assign(a, b, value, 0, 0, size - 1);
  }

  void add(int a, int b, int64_t value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      sum[vertex] += (right - left + 1) * value;
      add_op[vertex] = (add_op[vertex] == NO_OPT) ? value : add_op[vertex] + value;
      return;
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    add(a, b, value, LEFT(vertex), left, mid);
    add(a, b, value, RIGHT(vertex), mid + 1, right);

    sum[vertex] = sum[LEFT(vertex)] + sum[RIGHT(vertex)];
  }

  void add(int a, int b, int64_t value) {
    add(a, b, value, 0, 0, size - 1);
  }

  int64_t query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return 0;
    }

    if (a <= left && b >= right) {
      return sum[vertex];
    }

    lazy_propagation(vertex, right - left + 1);

    int mid = (left + right) / 2;
    int64_t l = query(a, b, LEFT(vertex), left, mid);
    int64_t r = query(a, b, RIGHT(vertex), mid + 1, right);
    return l + r;
  }

  int64_t query(int a, int b) {
    return query(a, b, 0, 0, size - 1);
  }
};

/*
int main(void)
{
  #define SIZE 8
  int arr[SIZE] = {2, 7, 1, 3, 5, 1, 2, 8};
  SegmentTree st(SIZE);

  for (int i = 0; i < SIZE; i++) {
    st.assign(i, i, arr[i]);
  }

  st.add(0, SIZE - 1, 0);
  st.add(0, 1, 0);
  st.add(2, 3, 0);

  st.add(0, 0, 1);
  st.add(0, SIZE - 1, 1);

  // 4 8 2 4 6 2 3 9
  st.assign(0, 0, 1);
  // 1 8 2 4 6 2 3 9

  st.add(0, SIZE - 1, 1);
  st.add(0, SIZE - 1, 1);
  // 3 10 4 6 8 4 5 11
  st.assign(0, SIZE - 1, 1);

  printf("%d\n", st.query(5, 7));

  return 0;
}
*/

int main(void)
{
  int n, m;
  scanf("%d %d", &n, &m);
  SegmentTree st(n);

  int op, arg1, arg2, arg3;
  for (int i = 0; i < m; i++) {
    scanf("%d", &op);
    if (op == 1) {
      scanf("%d %d %d", &arg1, &arg2, &arg3);
      st.assign(arg1, arg2 - 1, arg3);
    } else if (op == 2) {
      scanf("%d %d %d", &arg1, &arg2, &arg3);
      st.add(arg1, arg2 - 1, arg3);
    } else {
      scanf("%d %d", &arg1, &arg2);
      printf("%lld\n", st.query(arg1, arg2 - 1));
    }
  }
  return 0;
}

