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
    
    '''
    우선적으로 세가지 연산부터 집중해보자
    첫번째 연산 : 첫번째 원소를뽑아낸다. 이 연산을 수행하면 원래 큐의 원소가 a1...ak가 a2....ak가된다
    -> 결론적으로 deque에서 왼쪽에서 원소를 뽑는 연산이다
    두번쨰 연산 : 왼쪽으로 한칸 이동한다 연산을 수행하면 원래 큐 원소가 a1...ak가 a2...ak a1이 된다
    -> 결론적으로 popleft()연산 결과를 append()한 것과 같다
    세번째 연산 : 오른쪽으로 한칸 이동한다. 연산을 수행하면 원래 큐 원소가 a1...ak가 ak a1....ak-1이된다
    -> 결론적으로 pop()연산 결과를 appendleft()한 것과 같다.

    결론적으로 collections의 deque모듈을 사용하면 된다.

    하나 더 중요한것이 있는데, 2번 연산을 할지 3번 연산을 할지 기준을 세울 필요가 있다.

    예를 들어 다음과 같은 큐가 있다고 하자

    1 2 3 4 5 6 7

    내가 여기서 4를 1번연산으로 뽑고 싶다고 가정하자.

    3번 연산을 하게되면 총 4번을 해야되지만

    2번 연산을 하게되면 총 3번만 하면 된다.

    결론적으로 찾고자 하는 값의 index가(원소의 index를 알기위해서 .index(value) 메소드를 이용한다.) 전체 큐 길이를 2로 나눈 몫보다 작거나 같은 경우는 2번 연산을
    큐 길이를 2로 나눈 몫보다 큰 경우는 3번 연산을 수행해주는거로 알고리즘을 작성한다.
    '''

    def main(self):
        for y in range(len(self.needtoFind)):
            loop = True
            calculated = 0
            if self.body[0] == self.needtoFind[y]:
                    self.cal1()
            else:
                if self.body.index(self.needtoFind[y]) <= ((len(self.body) // 2)):
                    while self.body[0] != self.needtoFind[y]:
                        self.cal2()
                        calculated += 1
                    self.cal1()
                else:
                    while self.body[0] != self.needtoFind[y]:
                        self.cal3()
                        calculated += 1
                    self.cal1()
            self.calculatedCount += calculated
        print(self.calculatedCount)


finds = list(map(int, sys.stdin.readline().split()))
dq = deq(N, finds)
dq.main()
