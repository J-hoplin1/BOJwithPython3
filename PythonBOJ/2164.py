from typing import Any
from collections import deque
import sys

'''
N장의 카드
1~N까지의 번호 + 1번 카드가 제일위 N번 카드가 제일 아래

-> 제일 위에있는 카드를 바닥에 버린 후 그 다음 제일위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다

-> 결론적으로 1회 deque() 연산 후 2회 deque()연산값을 큐의 맨 뒤로 enque()한다는 소리

연산 순서 : deque() - deque() - enque()

collections 모듈의 deque메소드를 사용해서 풀어보자

이 알고리즘에서는 Queue Empty, Queue Full 에대한 경우는 생각하지 않는다.

'''


class queue(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.que = deque([],self.capacity)

    def enque(self, data) -> None:
        self.que.append(data)
    
    def deque(self) -> int:
        return self.que.popleft()
    
    def returnDataCount(self) -> int:
        return len(self.que)
    
    def printQueueFront(self) -> int:
        return print(self.que[0])

    def dump(self):
        print(*self.que, sep=' - ')

cards = int(sys.stdin.readline())
q = queue(cards)
for t in range(1,cards + 1): 
    q.enque(t)
loopBoolean = True
while q.returnDataCount() != 1:
    q.deque()
    if q.returnDataCount() == 1: # deque를 한 후에 큐내 데이터가 1개인 경우 break
        break
    else:
        q.enque(q.deque())

q.printQueueFront()
