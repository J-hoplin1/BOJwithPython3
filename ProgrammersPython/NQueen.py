# https://programmers.co.kr/learn/courses/30/lessons/12952

from typing import Any

class NQueen(object):
    
    def __init__(self,chessSize : int) -> None:
        # 정사각형에서의 대각선 개수 : (열 개수 * 2) -1
        self.row = [0] * chessSize # 각 열에 몇번째 행에 배치되었는지를 저장하는 배열이다.
        self.column = [False] * chessSize # 각 행에 퀸이 배치되었는지에 대해 저장하는 배열이다.
        self.diagnol1 = [False] * ((chessSize * 2) - 1)# 북동, 남서방향의 대각선 15개에 대해 배치 여부를 저장하는 배열이다.
        self.diagnol2 = [False] * ((chessSize * 2) - 1)  # 북서, 남동방향의 대각선 15개에 대해 배치 여부를 저장하는 배열이다.
        self.chessSize = chessSize
        self.totalPossibleCountOfArrangement = 0 #총 배치 횟수를 세는 변수
        
    def arrangeQueen(self,i : int) -> None:
        for j in range(self.chessSize):
            if ((not self.column[j]) and (not self.diagnol1[i + j]) and (not self.diagnol2[(i - j) + (self.chessSize -1)])):
                
                self.row[i] = j # 열에 행번호 정보를 저장한다.
                if i == (self.chessSize - 1):
                    self.totalPossibleCountOfArrangement += 1
                else:
                    self.column[j] = self.diagnol1[i + j] = self.diagnol2[(i - j) + (self.chessSize -1)] = True # 배치에 따른 두 대각선과, 행에 대해 True값을 넣어 다른 퀸이 배치되지 못하는것으로 지정
                    self.arrangeQueen(i + 1)
                    self.column[j] = self.diagnol1[i + j] = self.diagnol2[(i - j) + (self.chessSize -1)] = False# 위의 상황 해제(재귀과정에서의 대각선, 행, 열정보 초기화)
    
    
    def mainStream(self) -> None:
        self.arrangeQueen(0)
        return self.totalPossibleCountOfArrangement
    
    
def solution(n):
    a = NQueen(n)
    answer = a.mainStream()
    return answer
