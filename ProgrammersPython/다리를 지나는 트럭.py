from typing import Any
from collections import deque
# 문제풀이 : https://github.com/J-hoplin1/Problem-Solving/blob/master/ProgrammersPython/%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4/%EB%8B%A4%EB%A6%AC%EB%A5%BC%20%EC%A7%80%EB%82%98%EB%8A%94%ED%8A%B8%EB%9F%AD.md

class deq(object):

    def __init__(self, bridge_length,weight,truck_weights) -> None:
        self.bridge_length = bridge_length # 다리 총 길이
        self.weight = weight # 다리 최대 적재 무게
        self.truck_weights = deque(truck_weights,maxlen=len(truck_weights)) # 트럭 정보들
        self.totalTime = 0
        self.bridge = deque([]) # 다리
        self.done = 0 # 다리를 완전히 지난 트럭 개수
        self.totalWeight = 0 # 현재 트럭 무게
    
    def getInBridge(self) -> int:
        data = self.truck_weights.popleft()
        self.bridge.append([data,0]) # 들어갈때 [트럭, 트럭이 다리에 있는 시간] 으로 append()를 해준다.
        return data
    
    def getOutBridge(self) -> int:
        data = self.bridge.popleft()
        return data
    
    def peek(self) -> int:
        return self.truck_weights[0]

    def main(self) -> int:
        def onesecond() -> None: #1초 더해준다.
            popCal = 0 # popCal : 1초씩 더해준 후 pop()연산을 실행할 횟수를 더하는 변수이다. 1초씩 더해주는 연산과정에서 pop()연산을 실행하면 메모리 변동에 의한 pop()연산 혼동을 방지하기 위해서 사용한다. 
            for a in self.bridge: # 현재 다리에 있는 모든 트럭에 대해 1초씩 더해준다.
                a[1] += 1
                if a[1] == self.bridge_length: # 만약 해당 트력의 있었던 시간이 최대 길이와 동일하다면 popCal + 1을 해준다.
                    popCal += 1
                    self.done += 1
                else:
                    pass
            for _ in range(popCal): # 위 과정에서 나온 popCal만큼 pop연산 수행한다.
                self.totalWeight -= self.getOutBridge()[0]
        while self.done != self.truck_weights.maxlen:
            self.totalTime += 1
            try:
                # 매초 다음 트럭을 넣기 위해 시도한다.
                # 만약 다음 트럭 무게랑 현재 무게 합친게 최대 적재량보다 크면 넘어간다
                if self.peek() + self.totalWeight > self.weight:
                    pass
                # 아닌경우에는 추가한다.
                else:
                    self.totalWeight += self.getInBridge()
            except: # collections.deque 에서 peek()에 대한 예외를 처리하기 위해 사용한다. 마지막 트럭이 다리에 들어간 후에는 peek()을 하게되면 예외가 발생된다. 그 경우에는 어쩔수 없기에 pass하기 위해 try ~ except문을 사용해 처리했다.
                pass
            finally: # 공통적으로 새 트럭을 추가하든 추가하지 않든 1초 추가해주는 과정은 필수과정이다
                onesecond()
        self.totalTime += 1
        return self.totalTime
    
def solution(bridge_length, weight, truck_weights):
    dq = deq(bridge_length,weight,truck_weights)
    answer = dq.main()
    return answer
