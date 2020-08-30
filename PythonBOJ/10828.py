'''
Code written by J-Hoplin
Date of creation : 2019/09/23
URL : https://www.acmicpc.net/problem/10828
'''
#스택 리스트
stack = []

#출력순서
result = []

def push(a):
    stack.append(a)

def pop():
    if len(stack) == 0:
        result.append(-1)
    else:
        result.append(stack[-1])
        del stack[-1]

def size():
    result.append(len(stack))

def empty():
    if len(stack) == 0:
        result.append(1)
    else:
        result.append(0)

def top():
    if len(stack) == 0:
        result.append(-1)
    else:
        result.append(stack[-1])

io = int(input())

for a in range(0, io):
    a = input().split(' ')
    if a[0] == 'push':
        push(int(a[1]))
    elif a[0] == 'pop':
        pop()
    elif a[0] == 'size':
        size()
    elif a[0] == 'empty':
        empty()
    elif a[0] == 'top':
        top()

for b in range(0,len(result)):
    print(result[b])