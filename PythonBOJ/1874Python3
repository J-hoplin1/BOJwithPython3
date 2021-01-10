n = int(input())

stack = []
results = []

lastpushed = 1
shutdown = False
for e in range(n):
    num = int(input())

    while lastpushed <= num:
        stack.append(lastpushed)
        results.append('+')
        lastpushed += 1
    if stack[-1] == num:
        stack.pop()
        results.append('-')
    else:
        shutdown = True
        
if shutdown == True:
    print('NO')
else:
    for t in results:
        print(t)
