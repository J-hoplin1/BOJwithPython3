'''
카카오 2019 겨울 개발자 인턴십

URL : https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
'''
from collections import deque

class dollStack(object):

    def __init__(self,board):
        self.board = board
        self.prize = deque([]) 
        self.popped = 0 # 터진 인형개수
    
    def getPrize(self,moves):
        for u in self.board:
            if u[moves - 1]: # move는 1부터 시작하므로 인덱싱 조건에 맞춰주기 위해 -1, 인형이 있는 경우 연산시행
                try:
                    if u[moves - 1] == self.peekPrize(): # 뽑으려는 인형이 상품의 마지막에 있는 인형
                        self.prize.pop() # 상품 마지막 빼고
                        u[moves - 1] = 0 # 뽑으려던것도 없앤다.
                        self.popped += 2 # 터진 2개의 인형
                    else:
                        self.prize.append(u[moves - 1])
                        u[moves - 1] = 0
                except: #prize가 비었을 경우에 대한 예외
                    self.prize.append(u[moves - 1])
                    u[moves - 1] = 0
                break # 상품을 찾은거 자체에서 이후의 검색 이유 없음
            else:
                pass
        
    def peekPrize(self):
        return self.prize[-1]

    def getResult(self):
        return self.popped


def solution(board, moves):
    stk = dollStack(board)
    for i in moves:
        stk.getPrize(i)
    answer = stk.getResult()
    return answer


# print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4])) 테스트 케이스
