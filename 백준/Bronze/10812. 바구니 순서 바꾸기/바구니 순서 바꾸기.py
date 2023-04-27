n, m = map(int, input().split())
arr = [_+1 for _ in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    arr = arr[:i-1] + arr[k-1:j] + arr[i-1:k-1] + arr[j:]
for b in arr:
    print(b)