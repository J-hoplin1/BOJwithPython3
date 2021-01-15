from collections import deque
from typing import Any
import sys

'''
deque를 구현하자

명령

push_front : 정수 x를 덱의 앞에 넣는다.
push_back : 정수 x를 덱의 뒤에 넣는다.
pop_front : 덱의 가장 앞에 있는 수를 뺴고 그 수를 출력, 정수가 없는 경우에는 -1 출력
pop_back: 덱의가장 뒤에 있는 수를 뺴고, 그 수를 출력한다.정수가 없는 경우에는 -1 출력
size : 덱에 들어있는 정수 개수
empty : 덱이 비어있으면 1을 아니면 0을 출력
front : 덱의 가장 앞에 있는 정수 출력, 만약 덱에 들어있는 정수 없는 경우 -1출력
back : 덱의 가장 뒤에 있는 정수 출력, 만약 덱에 들어있는 정수가 없는 경우에는 -1출력
'''

class deq(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.deq = deque([],self.capacity)
    
    def empty(self) -> int:
        if not self.deq:
            return 1 # 비어있는 경우
        else:
            return 0 # 비어있지 않은 경우
    
    def push_front(self,data):
        self.deq.appendleft(data)
    

    def push_back(self,data):
        self.deq.append(data)
    
    def pop_front(self) -> int:
        if self.empty(): # 정수가 없는경우
            return -1
        else:
            return self.deq.popleft()
    
    def pop_back(self) -> int:
        if self.empty(): # 정수가 없는경우
            return -1
        else:
            return self.deq.pop()
    
    def size(self) -> int:
        return len(self.deq)
    
    def front(self) -> int:
        if self.empty(): # 정수가 없는경우
            return -1
        else:
            return self.deq[0]
    
    def back(self) -> int:
        if self.empty():
            return -1
        else:
            return self.deq[-1]


commandBlock = int(input())
results = list()
dq = deq(commandBlock)

for _ in range(commandBlock):
    command = sys.stdin.readline().split()
    commandBlock = command[0]
    if commandBlock == 'push_front':
        data = command[1]
        dq.push_front(data)
    elif commandBlock == 'push_back':
        data = command[1]
        dq.push_back(data)
    elif commandBlock == 'pop_front':
        results.append(dq.pop_front())
    elif commandBlock == 'pop_back':
        results.append(dq.pop_back())
    elif commandBlock == 'size':
        results.append(dq.size())
    elif commandBlock == 'empty':
        results.append(dq.empty())
    elif commandBlock == 'front':
        results.append(dq.front())
    elif commandBlock == 'back':
        results.append(dq.back())
    else:
        pass

for p in results:
    print(p)
