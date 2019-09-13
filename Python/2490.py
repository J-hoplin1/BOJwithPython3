li = []
for a in range(0, 3):
    io = input().split(' ')
    li.append(io)

for b in range(0, len(li)):
    if li[b].count('0') == 1:
        print('A')
    elif li[b].count('0') == 2:
        print('B')
    elif li[b].count('0') == 3:
        print('C')
    elif li[b].count('0') == 4:
        print('D')
    elif li[b].count('1') == 4:
        print('E')
