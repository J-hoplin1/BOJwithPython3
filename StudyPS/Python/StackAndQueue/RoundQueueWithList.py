from typing import Any

class FixedQueue(object):

    class Empty(Exception):
        pass
        #큐가 비었을 경우 예외 클래스
    
    class Full(Exception):
        pass
        #큐가 가득 찼을때의 예외 클래스
    
    def __init__(self,capacity: int) -> None:
        self.dataAmount = 0 #큐 안에 있는 데이터 양
        self.front = 0 # 데이터가 나가는 부분인 front
        self.rear = 0 # 데이터를 넣는 부분인 rear
        self.capacity = capacity # 전체 queue의 크기
        self.queue = [None] * capacity # 큐 크기
    
    def __len__(self) -> int:
        return self.dataAmount 
    
    def is_empty(self) -> bool:
        return self.dataAmount <= 0
    
    def is_full(self) -> bool:
        return self.dataAmount >= self.capacity
    
    def enque(self, data: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = data
        self.rear += 1
        self.dataAmount += 1
        if self.rear ==self.capacity: #rear의 logic index number가 전체 큐 용량과 같아지게 된다면 rear의 logic index number 을 0으로 초기화 한다.(배열 index한계를 넘게되므로)
            self.rear = 0
    
    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.queue[self.front]
        self.front += 1
        self.dataAmount -= 1
        if self.front == self.capacity: # front의 인덱스 값이 capacity와 같아질 경우에는 0으로 초기화 한다.
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que([self.front])
    
    def find(self, data) -> Any:
        for e in range(self.dataAmount):
            ix = (e + self.front) % self.capacity # front의 인덱스는 0이 아닐수도 있다.그렇기에 논리적 queue index의 front를 찾기 위해서는 논리 front index 에 값을 더한 후 전체 큐 용량을 나누어서 구해야 한다.
            if self.que[ix] == value:
                return ix
        return -1
    
    def count(self, data: Any) -> bool:
        c = 0
        for e in range(self.dataAmount):
            ix = (e + self.front) % self.capacity
            if self.que[ix] == data:
                c += 1
        return c
    
    def __contains__(self,value:Any) -> bool:
        return self.count(value)
    
    def clear(self) -> None:
        self.dataAmount = self.front = self.rear = 0
    
    def dump(self) -> None:
        if self.is_empty():
            print("Queue is Empty")
        else:
            for e in range(self.dataAmount):
                print(self.que[(e + self.front) % self.capacity], end = '')
            print()
