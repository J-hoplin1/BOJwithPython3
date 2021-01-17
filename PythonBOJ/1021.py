from collections import deque
from typing import Any
import sys

N , M = input().split()

N = int(N)
M = int(M)



class deq(object):

    def __init__(self,capacity, finds):
        self.capacity = capacity
        self.body = deque([t for t in range(1, self.capacity + 1)], self.capacity)
        self.needtoFind = finds
        self.calculatedCount = 0 # 2 3번 연산을 시행한 횟수
    
    def cal1(self): # 첫번째 원소 뽑아낸다
        return self.body.popleft()
    
    def cal2(self): # 왼쪽으로 한칸 이동한다.
        self.body.append(self.body.popleft())
    
    def cal3(self):
        self.body.appendleft(self.body.pop())
    
    def dump(self):
        print(*self.body, sep='  ')
    


    def main(self):
        for y in range(len(self.needtoFind)):
            loop = True
            calculated = 0
            indexMovement = 0 # 인덱스 이동
            if self.body[0] == self.needtoFind[y]:
                    self.cal1()
                    indexMovement += -1
            else:
                if self.body.index(self.needtoFind[y]) <= ((len(self.body) // 2)):
                    while self.body[0] != self.needtoFind[y]:
                        self.cal2()
                        calculated += 1
                        indexMovement += -1
                    self.cal1()
                    indexMovement += -1
                else:
                    while self.body[0] != self.needtoFind[y]:
                        self.cal3()
                        calculated += 1
                        indexMovement += 1
                    self.cal1()
                    indexMovement += -1
            self.calculatedCount += calculated
        print(self.calculatedCount)


finds = list(map(int, sys.stdin.readline().split()))
dq = deq(N, finds)
dq.main()
