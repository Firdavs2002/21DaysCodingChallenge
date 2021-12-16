s = input()
t = input()
flag = True

for i in range(len(s)):
    if (len(s) == len(t)) and (s[i] != t[-i-1]):
        flag = False
if len(s) == len(t) and flag:
    print('YES')
else:
    print('NO')