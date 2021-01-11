import sys

dataCapacity = int(input())

datas = list(map(int,sys.stdin.readline().split()))
result = [-1 for _ in range(dataCapacity)]
indexStack= []

for y in range(dataCapacity):
    try:
        while datas[y] > datas[indexStack[-1]]:
            result[indexStack.pop()] = datas[y]
    except: # index에 대한 Exception이 날 경우에는 오큰수가 없는 경우이므로 indexStack이 비어있다.
    # 즉 indexStack이 
        pass
    
    indexStack.append(y)

print(*result,sep=' ')
