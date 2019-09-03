ascend = [1,2,3,4,5,6,7,8]
descend = [8,7,6,5,4,3,2,1]

io = input()

li = io.split(' ')
for a in range(0,len(li)):
    li[a] = int(li[a])
if li == ascend:
    print('ascending')
elif li == descend:
    print('descending')
else:
    print('mixed')
