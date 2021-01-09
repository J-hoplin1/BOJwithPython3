from typing import Any

'''
Parenthesis String 

VPS 선별문제

기본적으로 parenthesis string에서() 형태를 만족해야 VPS가 된다.
결론적으로 기본적으로 주어진 괄호 문자열에서 ()를 모두 빼서 한번 정리해 줄 수 있는것이다

코드해석해보자

prs = input()
# 기본적으로 VPS를 만족시키는 ()를 제거하고 시작한다.
prs = list(filter(('').__ne__,list(prs.split('()'))))
prs = list(str(''.join(prs)))

이 부분이 1차적으로 VPS만족하는 문자열('()'형태)를 제거하고 다시 문자열로 합쳐주는 부분이다.

매직메소드인 __ne__ 는 __ne__(self,other) 가 기본형으로 x != y를 정의한다.
filter()메소드의 param : (필터(함수 혹은 메소드 가능) , 리스트)

우선 내가 이 문제를 풀면서 했던 발상은 
'(' 가 들어간 후 ')' 가 들어가면 VPS를 만족하지만

가장 중요한건 ')'가 들어간 후 '(' 가 들어가면 VPS를 만족하지 못한다.

그렇기에 필터링된 문자열에서 
'('가 나오게 되면 스택에 넣고, ')' 가 나오게 되면 다음과 같이 두가지 경우를 가진다

1) peek()의 결과가 '(' 인 경우에는 pop을 수행한다 
2)만약 그게 아닌 None인 경우에는 중도에 멈추었는지를 확인하는 bool 변수 shutdown값을 fasle로 바꾸고 for문을 break한다. 그 후 해당 연산에 대해 result를 NO 로 저장

shutdown없이 연산이 끝나게 되면 스택포인터값이 0( = 스택이 비었음) 임을 확인한 후 그에따른 결과값을 저장한다.

'''


class stack(object):

    def __init__(self, capacity: int = 60):
        self.capacity = capacity # 스택 최대 개수
        self.ptr = 0 # 스택 포인터
        self.__stk = [None] * capacity # 스택 본체
    
    def isEmpty(self) -> bool:
        return self.ptr <= 0

    def isFull(self) -> bool:
        return self.ptr >= self.capacity

    def push(self,data) -> None:
        self.__stk[self.ptr] = data
        self.ptr += 1

    def pop(self) -> None:
        if self.isEmpty():
            pass
        else:
            self.__stk[self.ptr - 1] = None
            self.ptr -= 1   
    
    def peek(self):
        return self.__stk[self.ptr - 1]

    def dump(self) -> None:
        print(self.__stk)
        print(self.ptr)
        print(self.trashStack)
        print('-'*30)

    def clear(self) -> None: # 다음 문자열 검사를 위해 스택 인스턴스 초기화
        self.ptr = 0
        self.__stk = [None] * self.capacity
        self.trashStack = list()

result = []

totalWrite = int(input())
stk = stack()
for e in range(totalWrite):
    prs = input()
    # 기본적으로 VPS를 만족시키는 ()를 제거하고 시작한다.
    prs = list(filter(('').__ne__,list(prs.split('()'))))
    prs = list(str(''.join(prs)))

    shutdown = False

    for t in prs:
        if t == '(':
            stk.push('(')
        elif t == ')':
            if stk.peek() == '(':
                stk.pop()
            else:
                shutdown = True
                break
    
    if not shutdown:
        if stk.ptr == 0:
            result.append('YES')
        else:
            result.append('NO')
        stk.clear()
    else:
        result.append('NO')
        stk.clear()

for e in result:
    print(e)

    
