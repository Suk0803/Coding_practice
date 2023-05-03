arr = []
a = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0, 'P': 0.0}
S = 0.0
s = 0.0
for _ in range(20):
    arr.append(list(input().split()))

for i in range(20):
        if arr[i][2] == 'P':
            continue
        else :
            S += float(arr[i][1]) * a[arr[i][2]]
            s += float(arr[i][1])

print(S/s)