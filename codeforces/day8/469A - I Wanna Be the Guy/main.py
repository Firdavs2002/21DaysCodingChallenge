n = int(input())

p = list(map(int, input().split()))[1:]
q = list(map(int, input().split()))[1:]

p.extend(q)
p.sort()

if len(set(p)) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')