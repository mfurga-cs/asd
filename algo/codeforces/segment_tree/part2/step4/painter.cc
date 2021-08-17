/*
  Drzewo przedziałowe na tablicy.
*/

#include <bits/stdc++.h>

typedef int int64;

#define WHITE false
#define BLACK true

#define LEFT(v)   (2 * (v) + 1)
#define RIGHT(v)  (2 * (v) + 2)

struct SegmentTree {
  int size;
  std::vector<bool> pref;
  std::vector<bool> suff;
  std::vector<int64> cnt;
  std::vector<int64> blk;
  std::vector<bool> upd;

  SegmentTree(int n) {
    size = std::pow(2, std::ceil(std::log(n)/std::log(2)));
    pref.assign(size * 2, WHITE);
    suff.assign(size * 2, WHITE);
    cnt.assign(size * 2, 0);
    blk.assign(size * 2, 0);
    upd.assign(size * 2, false);
  }

  void lazy_propagation(int vertex) {
    if (upd[vertex]) {
      pref[LEFT(vertex)] = static_cast<bool>(cnt[vertex]);
      suff[LEFT(vertex)] = static_cast<bool>(cnt[vertex]);
      pref[RIGHT(vertex)] = static_cast<bool>(cnt[vertex]);
      suff[RIGHT(vertex)] = static_cast<bool>(cnt[vertex]);
      cnt[LEFT(vertex)] = cnt[vertex];
      cnt[RIGHT(vertex)] = cnt[vertex];
      blk[LEFT(vertex)] = blk[vertex] / 2;
      blk[RIGHT(vertex)] = blk[vertex] / 2;
      upd[vertex] = false;
      upd[LEFT(vertex)] = true;
      upd[RIGHT(vertex)] = true;
    }
  }

  void merge(int vertex) {
    cnt[vertex] = cnt[LEFT(vertex)] + cnt[RIGHT(vertex)];
    blk[vertex] = blk[LEFT(vertex)] + blk[RIGHT(vertex)];
    pref[vertex] = pref[LEFT(vertex)];
    suff[vertex] = suff[RIGHT(vertex)];
    if (suff[LEFT(vertex)] == BLACK && pref[RIGHT(vertex)] == BLACK) {
      cnt[vertex]--;
    }
  }

  void update(int a, int b, bool value, int vertex, int left, int right) {
    if (b < left || a > right) {
      return;
    }

    if (a <= left && b >= right) {
      cnt[vertex] = static_cast<int64>(value);
      if (value) {
        blk[vertex] = right - left + 1;
      } else {
        blk[vertex] = 0;
      }
      pref[vertex] = value;
      suff[vertex] = value;
      upd[vertex] = true;
      return;
    }

    lazy_propagation(vertex);

    int mid = (left + right) / 2;
    update(a, b, value, LEFT(vertex), left, mid);
    update(a, b, value, RIGHT(vertex), mid + 1, right);

    merge(vertex);
  }

  void update(int64 a, int64 b, bool value) {
    update(a, b, value, 0, 0, size - 1);
  }

};

struct input {
  char color;
  int64 arg1;
  int64 arg2;
};

int main(void)
{
  int n;
  scanf("%d", &n);

  std::vector<input> data(n);
  int64 maxi = std::numeric_limits<int64>::min();
  int64 mini = std::numeric_limits<int64>::max();
  for (int i = 0; i < n; i++) {
    scanf(" %c %d %d", &data[i].color, &data[i].arg1, &data[i].arg2);
    maxi = std::max(maxi, data[i].arg1 + data[i].arg2 - 1);
    mini = std::min(mini, data[i].arg1);
  }

  if (mini < 0) {
    mini = std::abs(mini);
  } else {
    mini = 0;
  }

  SegmentTree st(mini + maxi + 1);

  char color;
  int64 arg1, arg2;

  for (int i = 0; i < n; i++) {
    //scanf(" %c %d %d", &color, &arg1, &arg2);
    color = data[i].color;
    arg1 = data[i].arg1;
    arg2 = data[i].arg2;
    st.update(mini + arg1, mini + arg1 + arg2 - 1, color == 'B');
    printf("%d %d\n", st.cnt[0], st.blk[0]);
  }

  return 0;
}

