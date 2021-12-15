n = int(input())
aGroup, bGroup, group = [], [], []

generalGroup = 0

for i in range(n):
    a, b = map(int, input().split())
    aGroup.append(a)
    bGroup.append(b)

for groups in range(n):
    generalGroup += bGroup[groups]
    generalGroup -= aGroup[groups]
    group.append(generalGroup)

print(max(group))
