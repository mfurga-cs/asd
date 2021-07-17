#include <bits/stdc++.h>
using namespace std;

int n, k;
vector<double> a;
vector<double> b;

int partition(vector<double> &c, int lo, int hi)
{
  double pivot = c[hi];
  int i = lo - 1;
  for (int j = lo; j < hi; j++) {
    if (c[j] < pivot) {
      i++;
      swap(c[i], c[j]);
    }
  }
  swap(c[i + 1], c[hi]);
  return i + 1;
}

double find_k_th(vector<double> &c, int k)
{
  int lo = 0, hi = c.size() - 1;
  int mid;

  while (lo <= hi) {
    mid = partition(c, lo, hi);
    if (mid == k) {
      return c[mid];
    }
    if (mid > k) {
      hi = mid - 1;
    } else {
      lo = mid + 1;
    }
  }
}

bool is_ok(double x)
{
  vector<double> c(n);

  for (int i = 0; i < n; i++) {
    c[i] = a[i] - b[i] * x;
  }

  sort(c.begin(), c.end());

  double sum = 0;
  for (int i = n - k; i < n; i++) {
    sum += c[i];
  }

/*
  double kth = find_k_th(c, c.size() - k);
  double sum = kth;
  int count = 1;

  for (int i = 0; i < n; i++) {
    if (c[i] > kth) {
      sum += c[i];
      count++;
    }
  }
*/

  //assert(count == k);
  return sum >= 0;
}

int main(void)
{
  scanf("%d %d", &n, &k);
  a.resize(n);
  b.resize(n);

  double l = numeric_limits<double>::max();
  double r = numeric_limits<double>::lowest();

  for (int i = 0; i < n; i++) {
    scanf("%lf %lf", &a[i], &b[i]);
    l = min(l, b[i]);
    r = max(r, a[i]);
  }

  l = 0;
  double m, res;

  for (int i = 0; i < 50; i++) {
    m = (l + r) / 2;
    if (is_ok(m)) {
      res = m;
      l = m;
    } else {
      r = m;
    }
  }

  printf("%.12f\n", res);

  return 0;
}
