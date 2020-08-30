count = 0
case = []
def hanoi(io,a,b,c):
    global count
    if io == 1:
        count += 1
        case.append([a,c])
    else:
        count += 1
        hanoi(io-1,a,c,b)
        case.append([a,c])
        hanoi(io-1,b,a,c)
io = int(input())
hanoi(io,'1','2','3')
print(count)
for a in range(0,len(case)):
    print(case[a][0],case[a][1])