#include <bits/stdc++.h>

typedef long long int64;

struct StackMaxMin {
  std::stack<int64> _s;
  std::stack<int64> _min;
  std::stack<int64> _max;

  void push(int64 x) {
    if (_s.empty()) {
      _s.push(x);
      _min.push(x);
      _max.push(x);
      return;
    }
    _s.push(x);
    _max.push(std::max(_max.top(), x));
    _min.push(std::min(_min.top(), x));
  }

  int64 pop() {
    int64 x = _s.top();
    _s.pop();
    _max.pop();
    _min.pop();
    return x;
  }

  bool empty() {
    return _s.empty();
  }

  int64 max() {
    return _max.top();
  }

  int64 min() {
    return _min.top();
  }
};

struct QueueMaxMin {
  StackMaxMin sl;
  StackMaxMin sr;

  int64 pop() {
    if (sl.empty()) {
      while (!sr.empty()) {
        sl.push(sr.pop());
      }
    }
    return sl.pop();
  }

  void push(int64 x) {
    sr.push(x);
  }

  int64 min() {
    int64 minl = !sl.empty() ? sl.min() : std::numeric_limits<int64>::max();
    int64 minr = !sr.empty() ? sr.min() : std::numeric_limits<int64>::max();
    return std::min(minl, minr);
  }

  int64 max() {
    int64 maxl = !sl.empty() ? sl.max() : std::numeric_limits<int64>::min();
    int64 maxr = !sr.empty() ? sr.max() : std::numeric_limits<int64>::min();
    return std::max(maxl, maxr);
  }

  bool empty() {
    return sl.empty() && sr.empty();
  }
};

int main(void)
{
  int64 n, k;
  scanf("%lld %lld", &n, &k);

  std::vector<int64> a(n);
  for (int64 i = 0; i < n; i++) {
    scanf("%lld", &a[i]);
  }

  QueueMaxMin queue;

  int64 i = 0, j = 0;
  int64 result = 0;

  for (j = 0; j < n; j++) {
    queue.push(a[j]);

    while (queue.max() - queue.min() > k) {
      queue.pop();
      i++;
    }

    result += (j - i + 1);
  }

  printf("%lld\n", result);

  return 0;
}

