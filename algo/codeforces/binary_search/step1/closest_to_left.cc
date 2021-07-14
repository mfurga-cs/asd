#include <cstdio>
#include <vector>

int binseach(const std::vector<long long> &nums, long long x)
{
  int left = 0, right = nums.size() - 1;
  int mid;
  int res = -1;

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
  scanf("%d %d", &n, &m);

  std::vector<long long> nums;
  long long x;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &x);
    nums.push_back(x);
  }

  for (int i = 0; i < m; i++) {
    scanf("%lld", &x);
    printf("%d\n", binseach(nums, x) + 1);
  }
  return 0;
}



