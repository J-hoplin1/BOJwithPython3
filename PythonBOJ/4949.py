from typing import Any
import sys

'''
VPS선별문제

입력 : 하나 또는 여러줄에 걸쳐서문자열이 주어진다. 각문자열은 영문 알파벳 공백 소괄호 대괄호
등으로 이루어져 있으며 길이는 100글자보다 작거나 같다.

입력의 종료조건으로 맨 마지막에 점 하나 들어온다.
-> 만약 입력이 . 이라면 종료

전에 풀어봤던 Parenthesis 감별 원리 응용
'''


class stack(object):
    def __init__(self,capacity: int = 500):
        self.capacity = capacity
        self.ptr = 0 # -> 소괄호 스택 포인터
        self.__stk = [None] * self.capacity # -> 소괄호
    
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
            pass
        else:
            self.__stk[self.ptr] = data
            self.ptr += 1
    
    def pop(self) -> None:
        if self.isEmpty():
            pass
        else:
            self.__stk[self.ptr-1] = None
            self.ptr -=1
    
    def peek(self) -> int:
        if self.isEmpty():
            pass
        else:
            return self.__stk[self.ptr - 1]
    

    def dump(self):
        print(f'stackpointer : {self.ptr}')
    
    def returnBalance(self) -> bool:
        return bool(self.ptr)



if __name__=="__main__":
    loop = True
    results = []
    while loop:
        stk = stack() # stack()인스턴스 선언
        balance = 'yes'
        shutdown = False
        paragraph = input()
        if paragraph == '.': # .을 입력하면 프로그램 종료 -> .만 있는 경우에는 balance 상태 YES이므로 YES로 반환
            loop = False
        else:
            paragraph = list(paragraph)
            for t in paragraph:
                if t == '(':
                    stk.push(t)
                elif t == '[':
                    stk.push(t)
                elif t == ')':
                    if stk.peek() == '(':
                        stk.pop()
                    else:
                        results.append("no")
                        shutdown = True
                        break
                elif t == ']':
                    if stk.peek() == '[':
                        stk.pop()
                    else:
                        results.append("no")
                        shutdown = True
                        break
                else:
                    pass
            if shutdown:
                pass
            else:
                if not stk.returnBalance():
                    results.append(balance)
                else:
                    results.append('no')
    for t in results:
        print(t)
