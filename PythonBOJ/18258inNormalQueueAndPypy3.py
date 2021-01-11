from typing import Any
import sys

'''
이 코드는 Pypy3를 이용해서 맞춘 문제입니다

round Queue를 이용하여서 문제를 풀어보자

큐 -> First In First Out의 원리를 가진다

push -> enque와 동일
pop -> deque와 동일
size -> 큐에 들어있는 정수 개수
empty -> 큐가 비어있을때 1 아니면 0
front : 큐 가장 앞에있는 정수 출력 큐 비었을때 -1출력
back : 리어의 정수 출력 큐 비어있을때는 -1 출력
'''

class queue(object):

    def __init__(self,capacity):
        self.front = 0
        self.rear = 0
        self.dataAmount = 0
        self.capacity = capacity
        self.que = [None] * self.capacity
    
    class isFull(Exception):
        pass

    def isEmpty(self): # -> empty
        if self.dataAmount:
            return 0 # 큐가 비어있지 않은 경우
        else:
            return 1 #큐가 비어있는 경우
    
    def isFull(self):
        return self.dataAmount >= self.capacity

    def enque(self, data): # -> push
        if self.isFull():
            raise isFull
        else:
            self.que[self.rear] = data
            self.rear += 1
            self.dataAmount += 1
            if self.rear == self.capacity:
                self.rear = 0
    
    def deque(self): # -> pop
        if bool(self.isEmpty()):
           return -1
        else:
            retData = self.que[self.front]
            self.que[self.front] = None
            self.front += 1
            self.dataAmount -= 1
            if self.front == self.capacity:
                self.front = 0
            return retData

    def size(self):# -> size
        return self.dataAmount
    
    def frontQ(self):
        if bool(self.isEmpty()):
            return -1
        else:
            return self.que[self.front]
    
    def backQ(self):
        if bool(self.isEmpty()):
            return -1
        else:
            return self.que[self.rear - 1]
        
    def dump(self):
        print(self.que)


commandCount = int(input())

q = queue(commandCount)
result = []
for i in range(commandCount):
    buffer = list(sys.stdin.readline().split())
    command = buffer[0]

    if command == 'push':
        data = int(buffer[1])
        q.enque(data)
    elif command == 'pop':
        dt = q.deque()
        result.append(dt)
    elif command == 'size':
        result.append(q.size())
    elif command == 'empty':
        result.append(q.isEmpty())
    elif command == 'front':
        result.append(q.frontQ())
    elif command == 'back':
        result.append(q.backQ())

for i in result:
    print(i)
