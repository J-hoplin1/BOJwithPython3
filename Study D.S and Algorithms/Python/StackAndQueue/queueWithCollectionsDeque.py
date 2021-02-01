'''
collections.deque를 이용해서 Queue를 구현해보자

collections.deque의 특징은 내부적으로 doubly 링크드 리스트로 표현이 된다.
양 끝 모두 접근이 가능하다. 하지만 deque의 가운데 부분 검색, 삽입, 제거는 느리다.

collections.deque의 주요 속성 및 함수 및 메소드

maxlen속성 : deque의 최대 크기를 나타내는 속성으로 읽기 전용이다. 크기 제한이 없으면 None이다.

append(x) : 흔히 아는 append

appendleft(x) : deque의 왼쪽에 x값을 append 해준다

clear() : deque의 모든 원소 삭제, 크기 0으로

copy() : deque의 얕은 복사 실행

count(x) : deque안에 x와 같은 원소의 개수를 반환

index(x) : deque안에 있는 x 가운데 가장 앞쪽에 있는 원소의 위치 반환

insert(i, x) : x를 deque의 i 위치에 삽입한다. 크기제한있는 deque인 경우 maxlen을 초과하게되면 IndexError 을 반환

pop() : pop연산

popleft() : pop연산을 왼쪽에 대해 실행

remove(value) : value의 첫번째 항목 삭제, 원소 없는 경우 ValueError 내보낸다.

reverse() : deque의 원소를 역순으로 재정렬, None 반화

'''

from typing import Any

class queue(object):

    def __init__(self,capacity):
        self.capacity = capacity
        self.que = deque([],self.capacity)
    
    #큐가 비었을 경우에 대한 예외 클래스
    class QueEmpty(Exception):
        pass

    class QueFull(Exception):
        pass
    
    def isEmpty(self):
        return not self.que # 비었을 경우 True 반환 아닌 경우 False반환
    
    def isFull(self):
        return len(self.que) >= self.que.maxlen
    
    def enque(self,data):
        if self.isFull():
            raise queue.isFull
        else:
            self.que.append(data)
    
    def deque(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            return self.que.popleft()
    
    def peek(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            return self.que[0]
    
    def count(self,searchData):
        self.que.count(searchData)
    
    def find(self,searchData):
        self.que.index(searchData)
    
    def __contains__(self,value):
        return self.count(value)
    
    def dump(self):
        if self.isEmpty():
            raise queue.isEmpty
        else:
            print(*self.que, end=' ')
