#include <bits/stdc++.h>
using namespace std;

int n, d;
vector<double> nums;

bool is_ok(double x, int &left, int &right)
{
  vector<double> arr = nums;
  vector<double> pref(n);
  vector<double> mins(n);
  vector<int>mins_idx(n);

  for (int i = 0; i < n; i++) {
    arr[i] -= x;
  }

  pref[0] = arr[0];
  mins[0] = pref[0];
  mins_idx[0] = 0;

  for (int i = 1; i < n; i++) {
    pref[i] = pref[i - 1] + arr[i];

    if (pref[i] < mins[i - 1]) {
      mins_idx[i] = i;
      mins[i] = pref[i];
    } else {
      mins_idx[i] = mins_idx[i - 1];
      mins[i] = mins[i - 1];
    }
  }

  if (pref[d - 1] >= 0) {
    left = 0;
    right = d - 1;
    return true;
  }

  int local_left = -1;
  int local_right = n;

  for (int r = d; r < n; r++) {
    if (pref[r] >= mins[r - d]) {
      if ((local_right - local_left) > (r - mins_idx[r - d] + 1)) {
        local_left = mins_idx[r - d] + 1;
        local_right = r;
      }
    }
  }

  if (local_right != n) {
    left = local_left;
    right = local_right;
    return true;
  }
  return false;
}

int main(void)
{
  scanf("%d %d", &n, &d);
  nums.resize(n);

  double avg = 0;

  for (int i = 0; i < n; i++) {
    scanf("%lf", &nums[i]);
    avg += nums[i];
  }

  avg /= static_cast<double>(n);

  int left, right;
  int bestl = 0, bestr = 0;

  double l = 0, r = 200.0;
  double m;
  double best = 0;

  for (int i = 0; i < 50; i++) {
    m = (l + r) / 2;
    if (is_ok(m, left, right)) {
      //printf("best: %f for %d %d\n", m, left, right);
      bestl = left;
      bestr = right;
      best = m;
      l = m;
    } else {
      r = m;
    }
  }

  if (avg >= best) {
    printf("%d %d\n", 1, n);
  } else {
    printf("%d %d\n", bestl + 1, bestr + 1);
  }


  return 0;
}

