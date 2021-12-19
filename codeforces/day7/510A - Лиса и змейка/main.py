n, m = map(int, input().split())
snake = ''
count = 0;

for i in range(n):
    count+=1
    for j in range(m):
        if i % 2 == 0 or (count % 4 != 0  and j == m-1) or (count % 4 == 0 and j == 0):
            snake += '#'
        else:
            snake += '.'
        
    snake += '\n'
    print(snake, end='')
    snake = ''