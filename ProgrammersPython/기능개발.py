'''
URL : https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
각 기능의 개발속도는 모두  다르다
뒤에있는 기능이 앞에있는 기능보다 먼저 개발될 수 있고, 이떄 뒤에있는 기능은 앞에있는 기능이 배포될 때 함께 배포된다.

배포되어야하는 순서대로 작업의 진도가 적힌 정수 배열 progress와 
각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질때 각 배포마다 몇개의 기능이 배포되는지를 return 하도록 solution완성

-> main 루프가 반복될때마다 우선적으로 progress를 더해준다
-> 그 후 pop()연산을 실행, 이 연산에는 100이 넘는 경우까지만 체크하고 break를 한 후에 결과를 answer에 넣는다. 결과가 0인경우는 넣지 않는다
'''
from collections import deque


class work(object):

    def __init__(self,progress,speed):
        self.progress = deque(progress,len(progress))
        self.speed = deque(speed,len(speed))
        self.answer = list()
    
    def addProgress(self):
        for a in range(len(self.progress)):
            self.progress[a] += self.speed[a]
    
    def isEmpty(self):
        return self.progress

    def peek(self):
        return self.progress[0]

    def pop(self):
        countEndProgress= 0
        for r in range(len(self.progress)):
            if self.progress[r] >= 100:
                countEndProgress += 1
            else:
                break
        for w in range(countEndProgress):
            self.progress.popleft()
            self.speed.popleft()
        if countEndProgress:
            self.answer.append(countEndProgress)
        else:
            pass
    
    def returnAnswer(self):
        return self.answer


def solution(progresses, speeds):
    works = work(progresses,speeds)
    while works.isEmpty():
        works.addProgress()
        works.pop()
    answer = works.returnAnswer()
    return answer
