n, k = map(int, input().split())
rounds = list(map(int, input().split()))
income = rounds[k-1]
count = 0

for round in rounds:
    if income <= round and round != 0:
        count += 1

print(count)