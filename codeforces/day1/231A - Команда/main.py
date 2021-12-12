n = int(input())
commands = []
count = 0

for i in range(n):
    commands.append(list(map(int, input().split(' '))))

for command in commands:
    if sum(command) > 1:
        count += 1

print(count)