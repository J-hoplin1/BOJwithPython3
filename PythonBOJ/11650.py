from typing import Any
import sys

'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표로 증가하는 순으로 ,x 좌표가 같으면
 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오

'''

count = int(input())
dit = dict()

for _ in range(count):
    x,y = map(int,input().split())
    if x not in dit.keys():
        dit[x] = list()
        dit[x] += [y]
    else:
        dit[x] += [y]
        dit[x] = sorted(dit[x])

for t in sorted(list(dit.keys())):
    for p in dit[t]:
        print(f'{t} {p}')

'''
from typing import Any
import sys

count = int(input())

arr = []

for _ in range(count):
    x,y = map(int,input().split())
    arr.append((x,y))


#.sort() 의 key param 에서 lambda 함수 사용해보기

#sort()의 key param은 정렬을 목적으로 하는 함수를 값으로 넣게된다.(lambda도 가능하고 일반 함수도 가능)
#key값을 기준으로 정렬되고, 기본값은 오름차순으로 정렬된다.

arr.sort(key=lambda x: (x[0],x[1])) # x[0]부터 정렬하고, 두번째 인자인 x[1] 정렬한다는 의미이다.
# arr = sorted(arr) 사실 그냥 이 sorted만 써도 됨
for t in arr:
    print(f'{t[0]} {t[1]}')
'''
