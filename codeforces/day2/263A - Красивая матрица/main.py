lengthMatrix = 5
matrix = []
x = 0
y = 0

for i in range(lengthMatrix):
    matrix.append(list(map(int, input().split())))
    try:
        x = matrix[i].index(1)
        if matrix[i][x] == 1:
            y = i
    except:
        continue

print(abs(abs(x - lengthMatrix) - abs(y - lengthMatrix)))