'''
이 문제는 C/C++정도의 속도를 요구한다
아래 코드는 맞지만 이를 Python3로 채점하게 된다면 틀리게 된다.

제출할때는 JIT 컴파일러가 달린 Pypy3로 제출하자
'''
from collections import deque

class stack(object):

    def __init__(self,capacity):
        self.stk = list()
    
    def push(self,data):
        self.stk.append(data)
    def pop(self):
        return self.stk.pop()
    def peek(self,data):
        return self.stk[0]


N = int(input())
stk = stack(N)
result = 0
previous = 0
for a in range(N):
    data = int(input())
    stk.push(data)

for _ in range(N):
    pop = stk.pop()
    if pop > previous:
        result += 1
        previous = pop
    else:
        pass
print(result)
