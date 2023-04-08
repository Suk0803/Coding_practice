n, m = map(int, input().split())
knows_truth = list(map(int, input().split()))
knows_truth = set(knows_truth[1:])
parties = []

for _ in range(m):
    l = list(map(int, input().split()))
    l = l[1:]
    parties.append(set(l))


count = len(parties)
for _ in range(m):
    for s in parties:
        intersection = s & knows_truth
        if len(intersection) > 0:
            knows_truth |= s
          
for s in parties:
    intersection = s & knows_truth
    if len(intersection) > 0:
        count -= 1

print(count)