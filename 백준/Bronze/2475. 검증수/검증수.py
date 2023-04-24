arr = list(map(int, input().split()))
arr = [num**2 for num in arr]
print(sum(arr)%10)