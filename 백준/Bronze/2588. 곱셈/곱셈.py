x = int(input())
y = list(input())
y = y[::-1]
result = []

for i in range(3):
    print(x * int(y[i]))
    result.append(x * int(y[i] + '0' * i))
print(sum(result))