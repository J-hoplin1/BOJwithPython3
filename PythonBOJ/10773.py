from typing import Any

'''
URL : https://www.acmicpc.net/problem/10773

잘못된 수를  부를때마다 0을 외쳐 가장 최근에 재민이가 쓴 수를 지우게 한다.
총 입력된 데이터들의 값들의 합을 구해야함


첫번째 입력값 -> 입력할 총 개수

ex) 예제입력

10
1
3
5
4
0
0
7
0
0
6

예제 입력 풀이 
1) 총 10개의 수를 입력한다
2) 1 3 5 4 를 입력한후 0을 입력했으니 1 3 5가 된다
3) 그 후 0을 또 입력했으니 1 3 이된다.
4) 그 후 7을 입력하였으니 1 3 7이 된다.
5) 0을 입력했으니 1 3이된다
6) 0을 입력했으니 1이된다
7) 6을 입력했으니 1 6이된다
8) 즉 총합 7

-> 결론적으로 '0'이라는 데이터는 스택 메소드의 pop()의 역할을 하는 것이다.

stack 클래스에는 기본적인 메소드만 구현한다

1) push
2) pop
3) sum
4) isEmpty
5) isFull

예외 클래스

1) StackEmpty
2) StackFull

클래스 구현후 테스트코드 작성
'''

class stack(object):

    def __init__(self, capacity) -> None:
        self.ptr = 0
        self.capacity = capacity
        self.__stk = [None] * capacity
        self.totalSum = 0

    class StackEmpty(Exception):
        pass
    
    class StackFull(Exception):
        pass
    
    def isEmpty(self) -> bool:
        return self.ptr <= 0

    def isFull(self) -> bool:
        return self.ptr >= self.capacity

    def push(self,data) -> None:
        if self.isFull():
            raise self.StackFull
        else:
            self.__stk[self.ptr] = data
            self.totalSum += data
            self.ptr += 1
    
    def pop(self) -> None:
        if self.isEmpty():
            raise self.StackEmpty
        else:
            self.totalSum -= self.__stk[self.ptr - 1]
            self.__stk[self.ptr - 1] = None
            self.ptr -= 1

    def dump(self) -> None:
        print(self.__stk)



totalCapacity = int(input())

stk = stack(totalCapacity)

for e in range(totalCapacity):
    data = int(input())
    if data == 0:
        stk.pop()
    else:
        stk.push(data)
    #stk.dump() -> 각 단계별 스택 변화를 보기위해

print(f'{stk.totalSum}')
