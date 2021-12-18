n = int(input())
love = list(map(int, input().split()))
count = 0
max = love[0]
min = love[0]

for l in love:
    if l > max:
        max = l
        count += 1
    if l < min:
        min = l
        count += 1

print(count)