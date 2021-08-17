
n, s = map(int, input().split())
a = list(map(int, input().split()))

k = 0 # this is the second pointer
C = [-1 for i in range(s)]
ans = float("+inf")

# Iterate the array with the first pointer
for i in range(0, n, 1):
    # Update C array
    for j in range(s, a[i], -1):
        C[j] = max(C[j], C[j-a[i]])
    C[a[i]] = i

    if C[s] >= k:
        ans = min(ans, i - C[s] + 1)
        k = C[s] + 1

print(ans if ans < int('inf') else -1)
