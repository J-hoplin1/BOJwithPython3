stack = []
results = []

n = int(input())
lastputNumber = 0 # 일부러 0부터 시작
shutdown = False

for t in range(n):
    s = int(input())
    
    if s >= lastputNumber + 1:
        while s != lastputNumber:
            stack.append(lastputNumber + 1)
            lastputNumber += 1
            results.append('+')
        stack.pop()
        results.append('-')
    
    elif s < lastputNumber + 1:
        if not stack:
            shutdown = True
            break
        elif s in stack:
            poppedRes = 0
            while s != poppedRes:
                poppedRes = stack.pop()
                results.append('-')
        else:
            shutdown = True
            break

if shutdown:
    print('NO')
else:
    for y in results:
        print(y)
