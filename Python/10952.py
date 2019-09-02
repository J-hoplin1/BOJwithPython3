li = []
while True:
    a,b = input().split(' ')
    if int(a) == 0 and int(b) == 0:
        break
    li.append(int(a) + int(b))

for a in range(0, len(li)):
    print(li[a])
