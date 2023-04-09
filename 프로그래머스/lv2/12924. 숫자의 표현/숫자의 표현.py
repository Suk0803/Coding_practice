def solution(n):
    count = 0
    for i in range(1, n + 1):
        Sum = 0
        for j in range(i, n + 1):
            Sum += j
            if Sum == n:
                count += 1
                break
            elif Sum > n:
                break

    return count
