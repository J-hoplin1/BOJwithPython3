a,b = input().split(' ')

q = int(a)
e = int(b)

if e < 45:
    if q - 1 < 0:
        q = 24
        print('{} {}'.format(q - 1, 60 - (45 - e)))
    else:
        print('{} {}'.format(q - 1, 60 - (45 - e)))
elif e >= 45:
    print('{} {}'.format(q, e - 45))
