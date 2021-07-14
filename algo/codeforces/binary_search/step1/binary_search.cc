#include <cstdio>
#include <vector>

bool binseach(const std::vector<long long> &nums, long long v)
{
  int left = 0, right = nums.size() - 1;
  int mid;
  while (left <= right) {
    mid = left + (right - left) / 2;
    if (nums[mid] == v) {
      return true;
    } else if (nums[mid] < v) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return false;
}

int main(void) {
  setvbuf(stdout, NULL, _IONBF, 0);

  int n, m;
  scanf("%d %d", &n, &m);

  std::vector<long long> nums;
  long long v;
  for (int i = 0; i < n; i++) {
    scanf("%lld", &v);
    nums.push_back(v);
  }

  for (int i = 0; i < m; i++) {
    scanf("%lld", &v);
    printf("%s\n", binseach(nums, v) == true ? "YES" : "NO");
  }
  return 0;
}



