/*
  Drzewo przedziałowe na tablicy. Szukanie liczby spójnych ciągów 1.

  Operacje:
    1. update(a, b, v) - ustaw na przedziale wartość 1.
    2. query_cnt(a, b) - zwraca liczbę segmentów na przedziala a do b.
    3. query_sum(a, b) - zwraca sumę jedynek na przedziale a do b.
*/

#include <cstdio>
#include <cmath>
#include <vector>
#include <limits>
#include <cassert>

typedef long long int int64;

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct row {
  int64 v;
  int64 l;
  int64 r;
};

struct SegmentTree {
  int size;
  std::vector<int64> pref;
  std::vector<int64> suff;
  std::vector<int64> cnt;
  std::vector<int64> sum;
  std::vector<bool> upd;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    pref.assign(size * 2, 0);
    suff.assign(size * 2, 0);
    cnt.assign(size * 2, 0);
    sum.assign(size * 2, 0);
    upd.assign(size * 2, false);
  }

  void lazy_propagation(int vertex) {
    if (upd[vertex]) {
      pref[LEFT(vertex)] = pref[vertex];
      suff[LEFT(vertex)] = suff[vertex];
      cnt[LEFT(vertex)] = cnt[vertex];
      sum[LEFT(vertex)] = sum[vertex] / 2;

      pref[RIGHT(vertex)] = pref[vertex];
      suff[RIGHT(vertex)] = suff[vertex];
      cnt[RIGHT(vertex)] = cnt[vertex];
      sum[RIGHT(vertex)] = sum[vertex] / 2;
      upd[vertex] = false;
    }
  }

  void merge(int vertex, int left, int right) {
    pref[vertex] = pref[left];
    suff[vertex] = suff[right];
    sum[vertex] = sum[left] + sum[right];

    cnt[vertex] = cnt[left] + cnt[right];
    if (suff[left] == 1 && pref[right] == 1) {
      cnt[vertex]--;
    }
  }

  void update(int a, int b, int value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      cnt[vertex] = value;
      pref[vertex] = value;
      suff[vertex] = value;
      sum[vertex] = (right - left + 1) * value;
      upd[vertex] = true;
      return;
    }

    lazy_propagation(vertex);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    merge(vertex, LEFT(vertex), RIGHT(vertex));
  }

  void update(int64 a, int64 b, int64 value) {
    if (a < 0 || b < 0) {
      printf("%lld %lld\n", a, b);
      assert(1 == 0);
    }
    update(a, b, value, 0, 0, size - 1);
  }

/*
  int64 query(int a, int b, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      return cnt[vertex];
    }

    lazy_propagation(vertex, left, right);

    int mid = (left + right) / 2;
    if (i <= mid) {
      return query(i, LEFT(vertex), left, mid);
    }
    return query(i, RIGHT(vertex), mid + 1, right);
  }

  int64 query(int i) {
    return query(i, 0, 0, size - 1);
  }
*/
};


int main(void)
{
  int n;
  scanf("%d", &n);

  std::vector<row> rows;

  int64 max = std::numeric_limits<int64>::min();
  char color;
  int arg1, arg2;
  for (int i = 0; i < n; i++) {
    row r;
    scanf(" %c %d %d", &color, &arg1, &arg2);
    r.l = arg1;
    r.r = arg1 + arg2 - 1;
    r.v = color == 'B';
    max = std::max(max, r.r);
    rows.push_back(r);
    if (r.l < 0 || r.r < 0) {
      printf("%d %d\n", r.l, r.r);
      volatile int d[1] = {0};
      d[10000] = 1;
      printf("%d\n", d[10000]);
    }
  }

  SegmentTree st(max + 1);

  for (int i = 0; i < n; i++) {
    row r = rows[i];
    st.update(r.l, r.r, r.v);
    printf("%lld %lld\n", st.cnt[0], st.sum[0]);
  }
  return 0;
}

