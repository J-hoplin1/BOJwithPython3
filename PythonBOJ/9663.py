from typing import Any

'''

N-Queen : Divide and Conquer Solve

N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제


- 퀸이 공격을 위해 움직일 수 있는 방위

1) 위, 아래

2) 왼쪽, 오른쪽

3) 남서,남동,북서.북동 대각선

이걸 바탕으로 분할과 한정작업을 해보자

1) 한 열(Row) 에는 하나의 퀸만 배치될 수 있다

2) 한 행(Column) 에는 하나의 퀸만 배치될 수 있다.

3) 한 대각선 라인에는 하나의 퀸만 배치될 수 있다.

퀸이 배치된 대각선이 몇번째 대각선인지를 구하는 방법은 아래와 같이 두가지 경우로 나눈다

1) 대각선이 북동, 남서방향인 경우에는 : 행의 번호와 열의 번호를 더하면 구할 수 있다.

2) 대각선이 북서, 남동방향인 경우에는 : 열의 번호에서 행의 번호를 뺀다음 7을 더해주면 구할 수 있다.

'''


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
        print(self.totalPossibleCountOfArrangement)
    

if __name__ == "__main__":
    chessSize = int(input())
    a = NQueen(chessSize)
    a.mainStream()

