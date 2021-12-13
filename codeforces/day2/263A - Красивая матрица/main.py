matrix = []
count = 0
x = 0
y = 0

for i in range(5):
    matrix.append(list(map(int, input().split())))
    try:
        x = matrix[i].index(1)
        if matrix[i][x] == 1:
            y = i
    except:
        continue

while x != 2:
    if x >= 3:
        x -= 1
    elif x <= 3:
        x += 1
    count += 1

while y != 2:
    if y >= 3:
        y -= 1
    elif y <= 3:
        y += 1
    count += 1

print(count)
