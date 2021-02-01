from typing import Any

'''
__len__() : 클래스형 인스턴스를 __len__()함수애 전달할 수 있다. 결론적으로 클래스형 인스턴스 a 가 있다고 하면 a.__len__()가 아닌 len(a)로 전달할 수 있다.

__contains__() : 클래스형 인스턴스에 멤버십 판단 연산자인 in을 적용할 수 있다. 위와 같이 클래스형 인스턴스 a가 있다고 하면 a.__contains__(x)를 x in a 로 할 수 있는 것이다.

'''



class fixedStack:

    class empty(Exception):
        pass
    class full(Exception):
        pass
    #initiate stack
    def __init__(self,capacity: int = 256) -> None:
        self.stk = [None] * capacity    #스택 본체
        self.capacity = capacity    #스택 크기
        self.ptr = 0    #스택 데이터 값(스택 포인터)
    
    def __len__(self) -> int:
        return self.ptr
    
    def isEmpty(self) -> bool:
        return self.ptr <= 0
    
    def isFull(self) -> bool:
        return self.ptr >= self.capacity

    def push(self,value: Any) -> None:
        #스택이 full 인 경우
        if self.isFull():
            raise fixedStack.full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    # 최상위 데이터 꺼내기
    def pop(self) -> Any:
        if self.isEmpty():
            raise fixedStack.empty
        self.ptr -= 1
        return self.stk[self.ptr]
    # 최상위 데이터 피킹
    def peek(self) -> Any:
        if self.isEmpty():
            raise fixedStack.empty
        return self.stk[self.ptr - 1]
    
    #모든 데이터 삭제
    def clear(self) -> None:
        self.ptr = 0
    
    #원소 검색 : 맨 앞에있는 index에 대해서만
    def find(self,value:Any)->Any:
        for a in range(self.ptr-1 , -1 , -1):
            if self.stk[a] == value:
                return a
        return -1
    

    #스택에 쌓여있는 데이터의개수를 구하여 반환한다.
    def count(self,value:Any) -> bool:
        c = 0
        for a in range(self.ptr):
            if self.stk[i] ==value:
                c+=1
        return c
    
    def __contains__(self,value:Any)->bool:
        return self.count(value)
    
    #모든 데이터를 바닥부터 꼭대기 순으로 출력
    def dump(self) -> None:
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.stk[:self.ptr])
