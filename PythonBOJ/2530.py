import sys
from typing import Any
'''
오븐구이 끝나는 시간 -> second 단위 

오븐의 앞면 -> 시가을 알려주는 디지털 시계 (시 / 분 / 초 단위)


결론 : 시작하는 시간과 요리 완성 시간이 초로 주어질 경우 , 오븐구이 끝나는 시간 계산

풀이

1) 주어지는 걸리는 시간은 초단위이다.
2) 총 걸리는 시간의 초를 req라고 하자
3) 걸리는 초는 req % 3600 % 60이다.
4) 걸리는 분은 req % 3600 // 60이다.
5) 걸리는 시는 req // 3600
6) 이제 입력되었던 시작시간에 하나씩 더해주자
7) 우선 (기존 초) + (걸리는 초)의 나머지가 걸린 초가 된다.
8) 그리고 (기존 초) + (걸리는 초)의 몫은 걸리는 분이 된다.
9) (기존 분) + (걸리는 분) + (8)에서 나온 추가되는 걸리는 분) 을 한 후 60으로 나눈 나머지가 종료시간의 분이 된다.
10) (기존 시) + (걸리는 시) + (9)에서 나온 추가되는 걸리는 시)를 더한 후 24를 나눈 나머지가 종료시간의 시가 된다.

예시

0 0 0 
172800

결과는 0 0 0이 되어야함

'''

dateNow = list(map(int, sys.stdin.readline().split()))
requiredTime = int(input())

rsec = requiredTime % 3600 % 60
rmin = requiredTime % 3600 // 60
rhr = requiredTime // 3600

sec = (rsec + dateNow[2]) % 60
addmin = (rsec + dateNow[2]) // 60

mint = (rmin + dateNow[1] + addmin) % 60
addhr = (rmin + dateNow[1] + addmin) // 60

hr = (rhr + dateNow[0] + addhr) % 24



print(f'{hr} {mint} {sec}')
