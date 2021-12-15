k, n, w = map(int, input().split())
count = []

for i in range(1, w+1):
    count.append(k*i)

if sum(count) - n < 0:
    print(0)
else:
    print(sum(count) - n)