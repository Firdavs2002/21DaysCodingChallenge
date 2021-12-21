k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
die = [k, l, m, n]
dragons = [0]*d

def dragonDie(dragons, count):
    for i in range(count-1, len(dragons), count):
        dragons[i] = count

for i in die:
    dragonDie(dragons, i)

result = [r for r in dragons if r not in [0]]
if 1 == k or 1 == l or 1 == n or 1 == m:
    print(d)
elif  d > n and d > m and d > l and d > k:
    print(len(result))
else:
    print(0)