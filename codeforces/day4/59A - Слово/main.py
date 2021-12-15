s = input()
lowers = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
uppers = ' '.join(lowers).upper().split()

lower = 0
upper = 0

for i in s:
    if i in lowers:
        lower += 1
    elif i in uppers:
        upper += 1

if lower >= upper:
    print(s.lower())
elif lower < upper:
    print(s.upper())