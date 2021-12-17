from math import ceil

n = int(input())

if n % 2 == 0:
    print(n // 2)
else:
    print(-ceil(n/2))
