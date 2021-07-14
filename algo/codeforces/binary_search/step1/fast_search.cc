#include <bits/stdc++.h>

int binsearch_right(const std::vector<long long> &nums, long long x) {
  int left = 0, right = nums.size() - 1;
  int mid;
  int res = nums.size() - 1;

  while (left <= right) {
    mid = left + (right - left) / 2;
    if (nums[mid] >= x) {
      res = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return res;
}

int binsearch_left(const std::vector<long long> &nums, long long x) {
  int left = 0, right = nums.size() - 1;
  int mid;
  int res = 0;

  while (left <= right) {
    mid = left + (right - left) / 2;
    if (nums[mid] <= x) {
      res = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return res;
}


int main(void) {
  setvbuf(stdout, NULL, _IONBF, 0);

  int n, m;
  scanf("%d", &n);

  std::vector<long long> nums;
  long long x;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &x);
    nums.push_back(x);
  }

  std::sort(nums.begin(), nums.end());

  scanf("%d", &m);

  int l, r;
  for (int i = 0; i < m; i++) {
    scanf("%d %d", &l, &r);
    if (l > nums[n - 1] || r < nums[0]) {
      printf("0\n");
    } else {
      int ll = binsearch_right(nums, l);
      int rr = binsearch_left(nums, r);
      printf("%d ", rr - ll + 1);
    }
  }
  puts("");

/*
  std::vector<long long> nums2;
  nums2.push_back(1LL);
  nums2.push_back(3LL);
  nums2.push_back(4LL);
  nums2.push_back(7LL);

  l = binsearch_right(nums2, 2);
  r = binsearch_left(nums2, 3);
  printf("%d\n", r - l + 1);
*/
  return 0;
}

