#include <bits/stdc++.h>

typedef long long int64;

#define MAX(a, b, c, d) std::max(std::max(std::max((a), (b)), (c)), (d))
#define MIN(a, b, c, d) std::min(std::min(std::min((a), (b)), (c)), (d))

int64 as, bs, cs, ds;
int64 ai = 0, bi = 0, ci = 0, di = 0;

std::vector<int64> a;
std::vector<int64> b;
std::vector<int64> c;
std::vector<int64> d;

void init()
{
  scanf("%lld", &as);
  a.resize(as);
  for (int64 i = 0; i < as; i++) {
    scanf("%lld", &a[i]);
  }

  scanf("%lld", &bs);
  b.resize(bs);
  for (int64 i = 0; i < bs; i++) {
    scanf("%lld", &b[i]);
  }

  scanf("%lld", &cs);
  c.resize(cs);
  for (int64 i = 0; i < cs; i++) {
    scanf("%lld", &c[i]);
  }

  scanf("%lld", &ds);
  d.resize(ds);
  for (int64 i = 0; i < ds; i++) {
    scanf("%lld", &d[i]);
  }

  std::sort(a.begin(), a.end());
  std::sort(b.begin(), b.end());
  std::sort(c.begin(), c.end());
  std::sort(d.begin(), d.end());
}

int64 *max(int64 &max_val)
{
  int64 max_val_loc = 0;
  int64 *max_idx_loc = nullptr;

  if (ai + 1 < a.size() && a[ai] > max_val_loc) {
    max_val_loc = a[ai];
    max_idx_loc = &ai;
  }

  if (bi + 1 < b.size() && b[bi] > max_val_loc) {
    max_val_loc = b[bi];
    max_idx_loc = &bi;
  }

  if (ci + 1 < c.size() && c[ci] > max_val_loc) {
    max_val_loc = c[ci];
    max_idx_loc = &ci;
  }

  if (di + 1 < d.size() && d[di] > max_val_loc) {
    max_val_loc = d[di];
    max_idx_loc = &di;
  }

  max_val = MAX(a[ai], b[bi], c[ci], d[di]);
  return max_idx_loc;
}

int64 *min(int64 &min_val)
{
  int64 min_val_loc = 100000000;
  int64 *min_idx_loc = nullptr;

  if (ai + 1 < a.size() && a[ai] < min_val_loc) {
    min_val_loc = a[ai];
    min_idx_loc = &ai;
  }

  if (bi + 1 < b.size() && b[bi] < min_val_loc) {
    min_val_loc = b[bi];
    min_idx_loc = &bi;
  }

  if (ci + 1 < c.size() && c[ci] < min_val_loc) {
    min_val_loc = c[ci];
    min_idx_loc = &ci;
  }

  if (di + 1 < d.size() && d[di] < min_val_loc) {
    min_val_loc = d[di];
    min_idx_loc = &di;
  }

  min_val = MIN(a[ai], b[bi], c[ci], d[di]);
  return min_idx_loc;
}


int main(void)
{
  init();

  int64 *min_idx, *max_idx;
  int64 min_val, max_val;
  int64 result_best = 100000000;
  int64 result[4] = {a[0], b[0], c[0], d[0] };

  for (int64 i = 0; i < (as + bs + cs + ds); i++) {
    min_idx = min(min_val);
    max_idx = max(max_val);

    if (max_val - min_val < result_best) {
      result_best = max_val - min_val;

      result[0] = a[ai];
      result[1] = b[bi];
      result[2] = c[ci];
      result[3] = d[di];
    }

    if (min_idx == nullptr) {
      break;
    }

    (*min_idx)++;
  }

  printf("%lld %lld %lld %lld\n", result[0], result[1], result[2], result[3]);

  return 0;
}

